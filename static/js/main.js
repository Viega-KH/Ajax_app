$(function () {
    $(document).on('submit', '#creat', function (e) {
        e.preventDefault();
        $.ajax({
            type: 'POST',
            url: 'add/',
            data: {
                name: $('#name').val(),
                last: $('#last').val(),
                phone: $('#phone').val(),
                addres: $('#addres').val(),
                liter: $('#liter').val(),
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },
            success: function (data) {
                $("#name").val('')
                $('#last').val('')
                $('#phone').val('')
                $('#addres').val('')
                $('#liter').val('')
                console.log(data)
                $("#content").load(location.href + " #content")
                // message content
                $("#creatModal").hide()
                $('#message').show()
                $('#message').css('display', 'flex')
                $('#sr-only').text(data)
                setTimeout(function () {
                    $('#message').hide()
                }, 1000)



            }
        })

    })

    //

    $(document).on('click', '#edit_btn', function (e) {
        e.preventDefault();

        var id = $(this).data('id');


        $.ajax({
            type: 'GET',
            url: 'get_product/' + id,
            success: function (response) {
                $('#name_id').val(response.name);
                $('#last_id').val(response.last);
                $('#phone_id').val(response.phone);
                $('#addres_id').val(response.addres);
                $('#liter_id').val(response.liter);
                $('#id_edit').val(response.id);
                $('#editModal').show()
            },
            error: function (xhr, errmsg, err) {
                console.log(xhr.status + ": " + xhr.responseText);
            }
        });
    });

    //

    $(document).on('submit', '#edit', function (e) {
        e.preventDefault();

        $.ajax({
            type: 'POST',
            url: $("#edit").attr("action"),
            data: {
                id_edit: $('#id_edit').val(),
                name_id: $('#name_id').val(),
                last_id: $('#last_id').val(),
                phone_id: $('#phone_id').val(),
                addres_id: $('#addres_id').val(),
                liter_id: $('#liter_id').val(),
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },
            success: function (data) {
                console.log($("#edit").attr("action"))
                $("#name_id").val('');
                console.log(data);
                $("#content").load(location.href + " #content");
                document.getElementById('editModal').style.display = 'none';
                $('#message-edit').show()
                $('#message-edit').css('display', 'flex')
                $('#sr-edit').text(data)
                setTimeout(function () {
                    $('#message-edit').hide()
                }, 1000)

            }
        })

    })

    $(document).on('click', '.close', function () {
        document.getElementById('editModal').style.display = 'none';
    })

    //

    $(document).on('click', '#delete_btn', function (e) {
        e.preventDefault();
        let id = $(this).data('id');

        $.ajax({
            type: 'POST',
            url: $("#delete_btn").attr("data-url"),
            data: {
                id: id,
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },
            success: function (data) {
                console.log(data);
                $("#content").load(location.href + " #content");
                // delete message
                $('#message-delete').show()
                $('#message-delete').css('display', 'flex')
                $('#sr-delete').text(data)
                setTimeout(function () {
                    $('#message-delete').hide();
                }, 1000);


            },
            error: function (xhr, errmsg, err) {
                console.log(xhr.status + ": " + xhr.responseText);
            }
        });



    }
    );


    $(document).on('click', '#open-creat', function () {
        $("#creatModal").show();
    })
    $(document).on('click', '#close-creat', function () {
        $("#creatModal").hide()
    })

    $(document).on('click', '#main-checkbox', function () {
        $('.task-checkbox').prop('checked', this.checked);
    })



    $(document).on('click', '#check_btn', function (e) {
        e.preventDefault();
        let selectedTasks = [];
        console.log(selectedTasks);
        $('.task-checkbox:checked').each(function () {
            selectedTasks.push($(this).val());
        });

        $.ajax({
            url: 'delete/check/',
            type: 'POST',
            data: {
                'task_ids[]': selectedTasks,
                'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()
            },
            success: function (response) {
                $("#root").load(location.href + " #root");
                console.log(response);
            }
        });
    });

















})






