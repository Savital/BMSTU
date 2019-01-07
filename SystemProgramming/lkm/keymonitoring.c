#include <linux/module.h>
#include <linux/interrupt.h>
#include <linux/slab.h>
#include <linux/keyboard.h>
#include <linux/notifier.h>
#include <linux/time.h>
#include <linux/proc_fs.h>
#include <linux/sched.h>
#include <linux/fs_struct.h>
#include <linux/uaccess.h>

#define KEYSTORE_ITEMS_MAX 128
#define KEYSTORE_ITEM_MAX_SIZE 80
#define SUCCESS 0

#define DRIVER_VERSION "v1.0"
#define DRIVER_AUTHOR "Savital"
#define DRIVER_DESC "Loadable kernel module for monitoring users' keyboard activity"

MODULE_AUTHOR(DRIVER_AUTHOR);
MODULE_DESCRIPTION(DRIVER_DESC);
MODULE_LICENSE("GPL");

static unsigned int comb_number;
static unsigned long search_time;
char *msg;
struct proc_dir_entry *proc_file;
static irqreturn_t irq_handler(int irq, void *dev_id);
static void workqueue_function(struct work_struct *work);
static struct workqueue_struct *queue = NULL;

static int isCapsLock = 0;
static size_t isRU = 0;

static unsigned char scancode = 0;
static unsigned long tmp = 0;
static int result = 0;
static int i = 0;

char* lowerKbdus[128] =
{
    "UK", "Escape", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-", "=",
    "Backspace", "Tab", "q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "[", "]", "Enter", "Control",
    "a", "s", "d", "f", "g", "h", "j", "k", "l", ";", "\'", "`",   "LeftShift",
    "\\", "z", "x", "c", "v", "b", "n", "m", ",", ".", "/",   "RightShift", "PrintScreen", "Alt", "SpaceBar",
    "CapsLock", "F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9", "F10",
    "NumLock", "ScrollLock", "HomeKey", "UpArrow", "PageUp", "-", "LeftArrow",
    "UK", "RightArrow", "+", "EndKey", "DownArrow", "PageDown", "InsertKey", "DeleteKey",
    "UK", "UK", "UK", "F11", "F12",
    "UK", "UK", "WinKey", "UK", "UK", "UK", "UK", "<KPEnter>", "<RCtrl>", "<KP/>", "<SysRq>", "<RAlt>", "UK",
    "<Home>", "<Up>", "<PageUp>", "<Left>", "<Right>", "<End>", "<Down>",
    "<PageDown>", "<Insert>", "<Delete>"	/* All other keys are undefined */
};

char* upperKbdus[128] =
{
    "UK", "Escape", "!", "@", "#", "$", "%", "^", "&", "&", "(", ")", "_", "+",
    "Backspace", "Tab", "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "{", "}", "Enter", "Control",
    "A", "S", "D", "F", "G", "H", "J", "K", "L", ":", "\"", "~", "LeftShift",
    "|", "Z", "X", "C", "V", "B", "N", "M", "<", ">", "?", "RightShift", "PrintScreen", "Alt", "SpaceBar",
    "CapsLock", "F1", "F2",   "F3",   "F4",   "F5",   "F6",   "F7",   "F8",   "F9", "F10",
    "NumLock", "ScrollLock", "HomeKey", "UpArrow", "PageUp", "-", "LeftArrow",
    "UK", "RightArrow", "+", "EndKey", "DownArrow", "PageDown", "InsertKey", "DeleteKey",
    "UK",   "UK",   "UK", "F11", "F12",
    0, 0, "WinKey"	/* All other keys are undefined */
};

char* lowerKbdusRU[128] =
{
    "UK", "Escape", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-", "=",
    "Backspace", "Tab", "й", "ц", "у", "к", "е", "н", "г", "ш", "щ", "з", "х", "ъ", "Enter", "Control",
    "ф", "ы", "в", "а", "п", "р", "о", "л", "д", "ж", "э", "ё",   "LeftShift",
    "\\", "я", "ч", "с", "м", "и", "т", "ь", "б", "ю", ".",   "RightShift", "PrintScreen", "Alt", "SpaceBar",
    "CapsLock", "F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9", "F10",
    "NumLock", "ScrollLock", "HomeKey", "UpArrow", "PageUp", "-", "LeftArrow",
    "UK", "RightArrow", "+", "EndKey", "DownArrow", "PageDown", "InsertKey", "DeleteKey",
    "UK",   "UK",   "UK", "F11",	"F12",
    0, 0, "WinKey"	/* All other keys are undefined */
};

char* upperKbdusRU[128] =
{
    "UK", "Escape", "!", "@", "#", "$", "%", "^", "&", "&", "(", ")", "_", "+",
    "Backspace", "Tab", "Й", "Ц", "У", "К", "Е", "Н", "Г", "Ш", "Щ", "З", "Х", "Ъ", "Enter", "Control",
    "Ф", "Ы", "В", "А", "П", "Р", "О", "Л", "Д", "Ж", "Э", "Ё", "LeftShift",
    "|", "Я", "Ч", "С", "М", "И", "Т", "Ь", "Б", "Ю", ",", "RightShift", "PrintScreen", "Alt", "SpaceBar",
    "CapsLock", "F1", "F2",   "F3",   "F4",   "F5",   "F6",   "F7",   "F8",   "F9", "F10",
    "NumLock", "ScrollLock", "HomeKey", "UpArrow", "PageUp", "-", "LeftArrow",
    "UK", "RightArrow", "+", "EndKey", "DownArrow", "PageDown", "InsertKey", "DeleteKey",
    "UK",   "UK",   "UK", "F11", "F12",
    0, 0, "WinKey"	/* All other keys are undefined */
};

unsigned long mtime(void)
{
	struct timespec t;
	getnstimeofday(&t);
	unsigned long mt = ((unsigned long) (t.tv_sec * 1000) + (unsigned long) (t.tv_nsec / 1000000));
	return mt;
}

struct keystore_item 
{
	int scancode;
	int state;
	int comb_number;
	unsigned long long down_time;
	unsigned long long search_time;
	struct keystore_item *next;
} *keystore;

struct log_queue 
{
	struct keystore_item *frnt, *rear;
} *log_queue_table;

void init_queue(struct log_queue *q) 
{
	q->frnt = NULL;
	q->rear = NULL;
}

int queue_isempty(struct log_queue *q) 
{
	if (q->frnt == NULL) 
	{
		q->rear = NULL;
		return 1;
	}  
	else 
		return 0;
}

void insert_in_queue(struct log_queue *q, int code, int state, int comb_number, unsigned long time, unsigned long time_up)
{
	if((q->rear == NULL) && (q->frnt == NULL)) 
	{
    	q->rear = kmalloc(sizeof(struct keystore_item), GFP_ATOMIC);
		q->rear->scancode = code;
		q->rear->state = state;
		q->rear->comb_number = comb_number;
		q->rear->down_time = time;
		q->rear->search_time = time_up;
		q->rear->next = NULL;
    	q->frnt = q->rear;
  	} 
	else 
	{
		struct keystore_item* temp = kmalloc(sizeof(struct keystore_item), GFP_ATOMIC);
		q->rear->next = temp;
    	temp->scancode = code;
    	temp->state = state;
    	temp->comb_number = comb_number;
		temp->down_time = time;
		temp->search_time = time_up;
		temp->next = NULL;
		q->rear = temp;
	}
}

struct keystore_item remove_from_queue(struct log_queue *q) 
{
	struct keystore_item ret;
	struct keystore_item *temp;
	ret.scancode = -1;
	ret.state = 0;
	ret.comb_number = -1;
	ret.down_time = 0;
	ret.search_time = 0;

	if (queue_isempty(q)) 
	{
		return ret;
	}
	ret.scancode = q->frnt->scancode;
	ret.state = q->frnt->state;
	ret.comb_number = q->frnt->comb_number;
	ret.down_time = q->frnt->down_time;
	ret.search_time = q->frnt->search_time;

	temp = q->frnt;
	q->frnt = q->frnt->next;
	kfree(temp);

	return ret;
}

static int find_key_rt(struct keystore_item *rt, int key) 
{
	int i, ret_idx = -1;
	for(i = 0; i < KEYSTORE_ITEMS_MAX; i++)
	{
		if (rt[i].scancode == key)
		{
			ret_idx = i;
			break;
		}
	}
	return ret_idx;
}

static irqreturn_t irq_handler(int irq, void *dev_id)
{
	struct work_struct *work = (struct work_struct*)kmalloc(sizeof(struct work_struct), GFP_KERNEL);
    if(work) 
	{
        INIT_WORK(work, workqueue_function);
		queue_work(queue, work);
    } 
	else 
	{
		printk(KERN_ERR "keymonitoring error: Could not allocate memory for work.\n");
	}

	return IRQ_HANDLED;
}

static void workqueue_function(struct work_struct *work) // 0x3A TODO
{
	scancode = inb(0x60);

	if (scancode & 0x80) // if released
	{
		scancode &= 0x7F;

		if (scancode >= 96)
	    {
	        kfree((void*)work);
	        return;
	    }

        if ((keystore[0x5B].scancode == 0x5B) && (keystore[0x39].scancode == 0x39))
            if (isRU)
                isRU = 0;
            else
                isRU = 1;

        tmp = (mtime() - keystore[scancode].down_time);
		tmp = tmp ? tmp : 1;

	    insert_in_queue(log_queue_table, scancode, keystore[scancode].state, keystore[scancode].comb_number, tmp, keystore[scancode].search_time);

		keystore[scancode].scancode = -1;
		keystore[scancode].state = 0;
		keystore[scancode].comb_number = -1;
		keystore[scancode].down_time = 0;
		keystore[scancode].search_time = 0;
	}
	else // If pressed
	{
	    if (scancode >= 96)
	    {
	        kfree((void*)work);
	        return;
	    }

        if (keystore[scancode].scancode == -1)
        {
            tmp = mtime();

            comb_number++;

            keystore[scancode].scancode = scancode;

            if (scancode == 0x3A)
                if (isCapsLock)
                    isCapsLock = 0;
                else
                    isCapsLock = 1;

            keystore[scancode].state = (((keystore[0x2A].scancode == 0x2A || keystore[0x36].scancode == 0x36) ? 1 : 0) + isCapsLock) % 2;

            if (isRU)
                keystore[scancode].state += 2;

		    keystore[scancode].comb_number = comb_number;
		    keystore[scancode].down_time = tmp;
		    keystore[scancode].search_time = tmp - search_time;
		    insert_in_queue(log_queue_table, scancode, keystore[scancode].state, keystore[scancode].comb_number, 0, keystore[scancode].search_time);

		    search_time = tmp;
		}
	}

	kfree((void*)work);
}

static int procfile_open(struct inode *i, struct file *f) 
{
	return SUCCESS;
}

static ssize_t procfile_read(struct file *filp, char *buffer, size_t count, loff_t *offp) 
{	
	
	int len = 0;
	if (queue_isempty(log_queue_table)) 
		return 0;
	struct keystore_item temp = remove_from_queue(log_queue_table);

	char* mychar = "UK";
	if (temp.state == 0)
	    mychar = lowerKbdus[temp.scancode];
	if (temp.state == 1)
	    mychar = upperKbdus[temp.scancode];
	if (temp.state == 2)
	    mychar = lowerKbdusRU[temp.scancode];
	if (temp.state == 3)
	    mychar = upperKbdusRU[temp.scancode];

	len += sprintf(msg, "%d %llu %llu %s %d\n", temp.scancode, temp.down_time, temp.search_time, mychar, temp.comb_number);

	copy_to_user(buffer, msg, len);

	return len;
}

const struct file_operations proc_file_fops = 
{
	.open = procfile_open,
	.read = procfile_read,
};

static int keymonitoring_init(void)
{
	msg = kmalloc(KEYSTORE_ITEM_MAX_SIZE*sizeof(char), GFP_ATOMIC);
	keystore	= kmalloc(KEYSTORE_ITEMS_MAX * sizeof(struct keystore_item), GFP_ATOMIC);
	log_queue_table = kmalloc(sizeof(struct log_queue), GFP_ATOMIC);
	init_queue(log_queue_table);
	search_time = 0;
	for (i = 0; i < KEYSTORE_ITEMS_MAX; i++) 
	{
		keystore[i].scancode = -1;
		keystore[i].state = 0;
		keystore[i].comb_number = -1;
		keystore[i].down_time = 0;	
		keystore[i].next = NULL;
	}
	comb_number = 0;
	
	proc_file = proc_create("keymonitoring", 0644, NULL, &proc_file_fops);
	if (proc_file == NULL) 
	{
		remove_proc_entry("keymonitoring", NULL);
		printk(KERN_ERR "keymonitoring error: Can't create proc file\n");
		return -ENOMEM;
	}

	result = request_irq(1, (irq_handler_t) irq_handler, IRQF_SHARED, "keymonitoring_rirq", (void*)(irq_handler));
	if (!result) 
	{
		queue = alloc_workqueue("keymonitoring_wq", WQ_MEM_RECLAIM | WQ_HIGHPRI, 0);
		if (!queue) 
		{
			free_irq(1, (void*)irq_handler);
			printk(KERN_ERR "keymonitoring error: Could not allocate memory for queue.\n");

			return -ENOMEM;
		}
	}	
	printk(KERN_INFO "keymonitoring info: successfully loaded!");	

	return 0;
}

static void keymonitoring_exit(void)
{	
	remove_proc_entry("keymonitoring", NULL);
	
	flush_workqueue(queue);
	destroy_workqueue(queue);
	free_irq(1, (void*)irq_handler);

	kfree(log_queue_table);
	kfree(keystore);	
	kfree(msg);

	printk(KERN_INFO "keymonitoring info: successfully unloaded!");
}

module_init(keymonitoring_init);
module_exit(keymonitoring_exit);

