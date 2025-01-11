
$(document).ready(function () {
    $(".add-note").click(function () {
        $("#note").val("");
        $("#note-form").attr("action", "/");
        $(".popup").removeClass("hidden").addClass("show");
    });

    $(".close-popup").click(function () {
        $(".popup").removeClass("show").addClass("hidden");
    });

    $(".confirm").click(function () {
        $(".alert").removeClass("alert").addClass("hidden");
    });

    $(".edit-note").click(function (e) {
        e.preventDefault();

        let noteId = $(this).attr("data-note_id");
        let noteText = $(`#note-${noteId} p`).text();

        $("#note").val(noteText)
        $(".popup").removeClass("hidden").addClass("show");
        $("#note-form").attr("action", `/edit_note/${noteId}`);
        $(".popup").removeClass("hidden").addClass("show");
    });

    $("#note-form").submit(function (e) {
        e.preventDefault();

        // Get the form action attribute
        let formAction = $(this).attr("action");

        $.post(formAction,
            // Serialize the form data
            $(this).serialize(),
            function (response) {
                if (response.status == "success") {
                    if (formAction === "/") {
                        // This is for adding a new note
                        location.reload();
                    } else {
                        // This is for editing a note
                        let updatedNote = response.updated_note;
                        let noteId = response.note_id;

                        $(`#note-${noteId} p`).text(updatedNote);
                        $(".popup").removeClass("show").addClass("hidden");
                    }
                }
            }, "json"
        );
    });

    $(".delete-note").click(function (e) {
        e.preventDefault();

        let noteId = $(this).attr("data-note_id");

        $.post(`/delete_note/${noteId}`,
            {
                csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val(), // CSRF token
            },
            function (response) {
                if (response.status == "success") {
                    $(`#note-${noteId}`).remove();
                }
            }, "json"
        )
    });
});

