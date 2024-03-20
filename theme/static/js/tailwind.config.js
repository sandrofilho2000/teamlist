window.addEventListener("DOMContentLoaded", function(){
    bg_color = document.querySelector("input#new_background_color")
    txt_color = document.querySelector("input#new_text_color")

    bg_color = bg_color ? bg_color.value : "#06aa48"
    txt_color = txt_color ? txt_color.value : "#fff"

    tailwind.config = {
        theme: {
          extend: {
            colors: {
              'clifford': '#da373d',
              'bg-primary': bg_color,
              'txt-primary': txt_color
            }
          }
        }
      }
})