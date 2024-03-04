async function get_colors_by_img() {
    imgName = $("img.league_main_img, img.team_main_img, img.country_flag").attr("src");
    imgClass = $("img.league_main_img, img.team_main_img, img.country_flag").attr("class");
    imgName = imgName.split("/")
    imgName = imgName[imgName.length - 1]
    folder = "leagues"

    if (imgClass.includes("team")) {
        folder = "teams"
    }

    else if (imgClass.includes("country")) {
        folder = "countries"
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

                return data
            })
            .catch(error => {
                console.error('There was a problem with the fetch operation:', error);
            });
    }

}



function apply_colors(background_color = false, text_color = false) {
    if (background_color) {
        $(".background-color").css("background-color", background_color).css("fill", background_color)
        $(".edit_component").css("border-color", background_color)
        $(".edit_component *").css("color", background_color)
        $(".edit_component *").css("fill", background_color)
        $("aside span").css("color", background_color)
        $("aside svg").css("fill", background_color)
        $("#id_background_color").val(background_color)
    }

    if (text_color) {
        $("body > nav *:not(small)").css("color", text_color)
        $("body > nav .line").css("background-color", text_color)
        $("body > nav input").css("border-bottom-color", text_color)
        $("body > nav").css("stroke", text_color)
        $(".data_list_ul").css("border-color", background_color)
        $("aside").css("background-color", text_color)
        $("aside").css("border-left-color", text_color)
        $(".edit_component").css("background-color", text_color)
        $("aside ul").css("background-color", text_color)
        $("#id_text_color").val(text_color)
        $("nav path, nav svg").css("fill", text_color).css("color", text_color)

    }

}


$(document).ready(async function () {
    const urlParams = new URLSearchParams(window.location.search);

    $(".open_palette").click(function (e) {
        e.stopPropagation()
        $(".colors_palette").toggleClass("hidden")
    })

    $(".close_open_palette").click(function () {
        $(".colors_palette").addClass("hidden")
    })

    $(".colors_palette").click(function (e) {
        e.stopPropagation()
    })

    if ($("img.league_main_img, img.team_main_img, img.country_flag").attr("src")) {
        
        var { background_color: background_color_from_img, text_color: text_color_from_img } = await get_colors_by_img()

        var background_color = document.querySelector("input#new_background_color")
        background_color.addEventListener("change", function (e) {
            new_color = e.target.value
            apply_colors(new_color, "")
            $(".update_color_form button").removeClass("opacity-40")
            $(".update_color_form button").removeClass("pointer-events-none")
        })

        var text_color = document.querySelector("input#new_text_color")
        text_color.addEventListener("change", function (e) {
            new_color = e.target.value
            apply_colors("", new_color)
            $(".update_color_form button").removeClass("opacity-40")
            $(".update_color_form button").removeClass("pointer-events-none")
        })



        $(".reset_colors").click(function (e) {
            let old_background_color = $("[old_background_color]").attr("old_background_color")
            let old_text_color = $("[old_text_color]").attr("old_text_color")
            apply_colors(old_background_color, old_text_color)
            background_color.value = old_background_color
            text_color.value = old_text_color
            $(".update_color_form button").addClass("pointer-events-none")
            $(".update_color_form button").addClass("opacity-40")

        })


        $(".get_by_ia_colors").click(async function (e) {
            let { background_color: background_color_from_img, text_color: text_color_from_img } = await get_colors_by_img()
            apply_colors(background_color_from_img, text_color_from_img)
            background_color.value = background_color_from_img
            text_color.value = text_color_from_img

            $(".update_color_form button").removeClass("opacity-40")
            $(".update_color_form button").removeClass("pointer-events-none")
        })


        $(".reverse_colors").click(async function (e) {
            let bg_color = background_color.value
            let txt_color = text_color.value
            let old_text_color = $("[old_text_color]").attr("old_text_color")

            background_color.value = txt_color
            text_color.value = bg_color

            apply_colors(txt_color, bg_color)

            if (txt_color !== old_text_color) {
                $(".update_color_form button").addClass("pointer-events-none")
                $(".update_color_form button").addClass("opacity-40")

            } else {
                $(".update_color_form button").removeClass("opacity-40")
                $(".update_color_form button").removeClass("pointer-events-none")
            }
        })


        var has_background_color = background_color.classList.contains("has_color")
        var has_text_color = text_color.classList.contains("has_color")

        if (has_background_color) {
            apply_colors(background_color.value, "")
            background_color.setAttribute("old_background_color", background_color.value)
        }

        if (has_text_color) {
            apply_colors("", text_color.value)
            text_color.setAttribute("old_text_color", text_color.value)
        }

        if (!has_text_color && !has_background_color) {
            apply_colors(background_color_from_img, text_color_from_img)
            background_color.value = background_color_from_img
            text_color.value = text_color_from_img
            background_color.setAttribute("old_background_color", background_color_from_img)
            text_color.setAttribute("old_text_color", text_color_from_img)
        }
    }


})

