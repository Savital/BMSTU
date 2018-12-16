// using jQuery
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

function send()
{
    alert("Request sended!")
    var req_url = $("input[name='url']").val();
	var req_method = $("select[name='method']").val();
	$.ajax
	    ({
		    url: "send/",
		    method: "POST",
		    data:
		    {
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