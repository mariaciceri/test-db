
$(document).ready(function () {
    // Display the popup form when the add note button is clicked
    $(".add-note").click(function () {
        $("#note").val("");
        $("#note-form").attr("action", "/");
        $(".popup").removeClass("hidden").addClass("show");
        $(".overlay").removeClass("hidden").addClass("show");
    });

    // Close the popup form when the close button is clicked
    $(".close-popup").click(function () {
        $(".popup").removeClass("show").addClass("hidden");
        $(".overlay").removeClass("show").addClass("hidden");
    });

    /** 
    * Open the popup form when the edit note button is clicked
    * and populate the form with the note text
    */
    $(".edit-note").click(function (e) {
        e.preventDefault();

        let noteId = $(this).attr("data-note_id");
        let noteText = $(`#note-${noteId} p`).text();

        $("#note").val(noteText)
        $(".popup").removeClass("hidden").addClass("show");
        $(".overlay").removeClass("hidden").addClass("show");
        $("#note-form").attr("action", `/edit_note/${noteId}`);
    });

    /**
     * Submit the form data when the note form is submitted
     */
    $("#note-form").submit(function (e) {
        e.preventDefault();

        // Get the form action attribute to pass to post request
        let formAction = $(this).attr("action");

        $.post(formAction,
            // Serialize the form data to pass to the post request
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
                        $(".overlay").removeClass("show").addClass("hidden");
                    }
                }
            }, "json"
        );
    });

    /**
     * Delete a note when the delete note button is clicked
    */
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

    /**
     * Display fields in accordion style when screen is less than 768px
     * and checks the screen size on window resize
     */
    function checkScreenSize() {
        if ($(window).width() <= 768) {
            $(".transactions-display").off("click").click(function () {
                $(".transactions-list").toggle("slow");
            });

            $(".plans-display").off("click").click(function () {
                $(".plans-list").toggle("slow");
            });

            $(".notes-display").off("click").click(function () {
                $(".notes-accordion").toggle("slow");
            });
        }
        else {
            $(".transactions-list").show("slow");
            $(".plans-list").show("slow");
            $(".notes-accordion").show("slow");

            $(".transactions-display").off("click");
            $(".plans-display").off("click");
            $(".notes-display").off("click");
        }
    }

    checkScreenSize();
    $(window).resize(checkScreenSize);

});

