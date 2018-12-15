function send()
{
    alert("Hello");
    var req_url = $("input[name='url']").value;
	var req_method = $("select[name='method']").value;
	$.ajax
	    ({
		    url: "send/",
		    method: "POST",
		    data:
		    { csrfmiddlewaretoken: "{{ csrf_token }}",
			    url: req_url,
			    method: req_method
		    },
		    success: function (data)
		    {
			    var body =  data.content;
			    var headers =  data.headers;
			    document.getElementsByName("resp")[0].innerHTML = headers + body;
		    }
        });
};