
function test_color(color_1, color_2) {
    
    setInterval(()=>{
        $("body > nav").css("background-color", color_1)
        $("body > nav h1 a").css("color", color_2)
        console.log(color_1, color_2)
    }, 3000)
}


let colors = [[0, 0, 0], [214, 24, 46], [244, 23, 58], [139, 198, 131], [255, 255, 255]]

colors.forEach((color, index)=>{
    let curr_color, last_color
    
    if (index === 0) {
        curr_color = colors[0]
        last_color = colors[colors.length - 1]
    }else{
        curr_color = colors
        last_color = colors[index - 1]
    }

    let color_1 = `rgb(${last_color[0]}, ${last_color[1]}, ${last_color[2]})`
    let color_2 = `rgb(${curr_color[0]}, ${curr_color[1]}, ${curr_color[2]})`
    
    test_color(color_1, color_2)
})


