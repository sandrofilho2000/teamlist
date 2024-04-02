// Function to fetch colors based on the image
async function get_colors_by_img() {
    let imgName = $("img.league_main_img, img.team_main_img, img.country_flag").attr("src");
    let imgClass = $("img.league_main_img, img.team_main_img, img.country_flag").attr("class");
    imgName = imgName.split("/");
    imgName = imgName[imgName.length - 1];
    let folder = "leagues";

    if (imgClass.includes("team")) {
        folder = "teams";
    } else if (imgClass.includes("country")) {
        folder = "countries";
    }

    if (imgName) {
        return fetch(`/api/design_ui?img_name=${imgName}&folder=${folder}`)
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                return data;
            })
            .catch(error => {
                console.error('There was a problem with the fetch operation:', error);
            });
    }
}

// Function to enable button
function enable_button() {
    $(".update_color_form button").removeClass("opacity-40");
    $(".update_color_form button").removeClass("pointer-events-none");
}

// Function to disable button
function unable_button() {
    $(".update_color_form button").addClass("opacity-40");
    $(".update_color_form button").addClass("pointer-events-none");
}

// Function to apply colors
function apply_colors(background_color = false, text_color = false) {
    if (background_color) {
        $(".table_tr:not(:has(th)), .card, .detail_card").hover(function () {
            $(this).css("background-color", background_color);
        }, function () {
            $(this).css("background-color", "");
        });

        $("#id_background_color").val(background_color);
    }

    if (text_color) {
        $(".table_tr:not(:has(th)), .card, .detail_card").hover(function () {
            $(this).find("*").css("color", text_color);
        }, function () {
            $(this).find("*").css("color", ""); // Reset to default text color when not hovered
        });

        $("#id_text_color").val(text_color);
    }
}

// Document ready function
$(document).ready(async function () {
    const urlParams = new URLSearchParams(window.location.search);

    // Event listener to toggle colors palette
    $(".open_palette").click(function (e) {
        e.stopPropagation();
        $(".colors_palette").toggleClass("hidden");
    });

    // Event listener to close colors palette
    $(".close_open_palette").click(function () {
        $(".colors_palette").addClass("hidden");
    });

    // Prevent closing palette on click inside
    $(".colors_palette").click(function (e) {
        e.stopPropagation();
    });

    // Get colors by image and apply them
    if ($("img.league_main_img, img.team_main_img, img.country_flag").attr("src")) {
        var { background_color: background_color_from_img, text_color: text_color_from_img } = await get_colors_by_img();

        // Event listener for background color change
        var background_color = document.querySelector("input#new_background_color");
        background_color.addEventListener("change", function (e) {
            let new_color = e.target.value;
            apply_colors(new_color, "");
            enable_button();
        });

        // Event listener for text color change
        var text_color = document.querySelector("input#new_text_color");
        text_color.addEventListener("change", function (e) {
            let new_color = e.target.value;
            apply_colors("", new_color);
            enable_button();
        });

        // Event listener for resetting colors
        $(".reset_colors").click(function (e) {
            let old_background_color = $("[old_background_color]").attr("old_background_color");
            let old_text_color = $("[old_text_color]").attr("old_text_color");
            apply_colors(old_background_color, old_text_color);
            background_color.value = old_background_color;
            text_color.value = old_text_color;
            unable_button();
        });

        // Event listener for getting colors by image analysis
        $(".get_by_ia_colors").click(async function (e) {
            let { background_color: background_color_from_img, text_color: text_color_from_img } = await get_colors_by_img();
            apply_colors(background_color_from_img, text_color_from_img);
            background_color.value = background_color_from_img;
            text_color.value = text_color_from_img;
            enable_button();
        });

        // Event listener for reversing colors
        $(".reverse_colors").click(async function (e) {
            let bg_color = background_color.value;
            let txt_color = text_color.value;
            let old_text_color = $("[old_text_color]").attr("old_text_color");

            background_color.value = txt_color;
            text_color.value = bg_color;

            apply_colors(txt_color, bg_color);
            enable_button();
        });

        // Check if background and text colors exist and apply them
        var has_background_color = background_color.classList.contains("has_color");
        var has_text_color = text_color.classList.contains("has_color");

        if (has_background_color) {
            apply_colors(background_color.value, "");
            background_color.setAttribute("old_background_color", background_color.value);
        }

        if (has_text_color) {
            apply_colors("", text_color.value);
            text_color.setAttribute("old_text_color", text_color.value);
        }

        if (!has_text_color && !has_background_color) {
            apply_colors(background_color_from_img, text_color_from_img);
            background_color.value = background_color_from_img;
            text_color.value = text_color_from_img;
            background_color.setAttribute("old_background_color", background_color_from_img);
            text_color.setAttribute("old_text_color", text_color_from_img);
        }
    }
});
