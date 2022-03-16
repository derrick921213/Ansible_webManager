var $sidebar = $('.control')
var $dark_mode_checkbox = $('<input />', {
    id: 'dark',
    type: 'button',
    value: "DarkMode",
    class: 'mr-1',
    css: {
        "width": "85px",
        "height": "35px",
        "font-size": "15px",
        "line-height": "25px",
        "text-align": "top",
        "margin-left": "10px",
        "border-radius": "10px",
        "background-color": "#343a40",
        "color": "#fff",
        "padding": "0px"
    }
}).on('click', function () {
    if ($('body').hasClass('dark-mode')){
        $('body').removeClass('dark-mode');
    }else {
        $('body').addClass('dark-mode');
    }
})

var $logout = $('<input />', {
    type: 'button',
    value: "LogOut",
    class: 'mr-1',
    css: {
        "width": "55px",
        "height": "35px",
        "font-size": "15px",
        "line-height": "25px",
        "text-align": "top",
        "margin-left": "2.5px",
        "border-radius": "10px",
        "background-color": "#343a40",
        "color": "#fff",
        "padding": "0px"
    }
}).on('click', function () {
    window.location.href ='/logout';
})

$sidebar.append($('<div />', { 
    class: 'mb-0 p-0 control-sidebar-content',
    css: {
        "display": "inline-block",
        "vertical-align": "baseline"
    }
}).append($dark_mode_checkbox).append($logout))

$(function () {
    $("#content_menu li a").click(function () {
        console.log($(this));
        $(this).siblings('#content_menu li a').removeClass('active');  // 删除其他兄弟元素的样式
        $(this).addClass('active');
    });
});
$(document).ready(function () {
    $("#content_menu li a").each(function () {
        $this = $(this);
        if ($this[0].href == String(window.location)) {
            $this.removeClass("active");
            $this.addClass("active");  //active表示被选中效果的类名
        }
    });
}); 
