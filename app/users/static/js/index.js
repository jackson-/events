$(document).ready(function(){


    $(".event").mouseenter(function(){
        if ($(this).attr("id") != "table-labels"){
            $(this).css({"background-color": "#d6d6c2"})
            $(this).mouseleave(function(){
                $(this).css({"background-color": "white"})
            })
        }
    })

    $(".editor").click(function(event){
        event.preventDefault();
        var ev_id = $(this).parent().parent().attr("id")
        $.get("/edit/"+ev_id, function(data){
            $('.date-input').val(data.date)
            $('.time-input').val(data.time)
            $('.location-input').val(data.location)
            $('.people-input').val(data.people)
            $('.description-input').val(data.description)
        })

        $('#edit-form').submit(function(event){
            event.preventDefault();
            event.stopPropagation();
            var form_data = $(this).serialize();
            $.post("/edit/"+ev_id, form_data, function(data){
                $('#myModal').modal('hide');
                location.reload();
            })
        })
    })

    $(".deleter").click(function(event){
        event.preventDefault();
        var ev_id = $(this).parent().parent().attr("id")
        console.log(ev_id);
        $.post("/delete/"+ev_id, function(data){
            console.log(data);
            $("#"+ev_id).remove();
            $("#hr-"+ev_id).remove();
        })
    })

    $(".past-deleter").click(function(event){
        event.preventDefault();
        var ev_id = $(this).parent().parent().attr("id")
        console.log(ev_id);
        $.post("/pastdelete/"+ev_id, function(data){
            console.log(data);
            $("#"+ev_id).remove();
            $("#hr-"+ev_id).remove();
        })
    })
})
