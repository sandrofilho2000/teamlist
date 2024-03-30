// Function to toggle menu
$(".toggle-menu").click(() => {
    $("body").toggleClass("menu-active");
});


$(".search_field input").focus(() => {
    $(".search_recomendation").removeClass("hidden");
});


function slugify(str) {
    str = str.replace(/^\s+|\s+$/g, ''); // Remove espaços em branco do início e do final da string
    str = str.toLowerCase(); // Converte a string para minúsculas
    const from = "àãáäâèéëêìíïîòóöõôùúüûñç·/_,:;";
    const to   = "aaaaaeeeeiiiioooõouuuunc------"; // Substituições de caracteres especiais
    for (let i = 0, l = from.length; i < l; i++) {
      str = str.replace(new RegExp(from.charAt(i), 'g'), to.charAt(i));
    }
    str = str.replace(/[^a-z0-9 -]/g, '') // Remove caracteres especiais
             .replace(/\s+/g, '-') // Substitui espaços por hífens
             .replace(/-+/g, '-'); // Remove múltiplos hífens
    return str;
  }

// Function to shorten name
function enshort_name(value) {
    return value.length > 24 ? value.substring(0, 24) + "..." : value;
}

// Function to handle keyup event on search input
var typingTimer;
$(".search_field input").keyup((e) => {
    $(".datalist_ul").html("");
    $(".datalist_ul").removeClass("active")
    
    clearTimeout(typingTimer);
    if (e.target.value) {
        $(".datalist_skeleton.skeleton-loading").fadeIn();
        $("html").addClass("overflow-hidden")

        typingTimer = setTimeout(() => {
            const query = slugify(e.target.value.trim())
            const apiUrl = `/search_items/${query}/`;

            fetch(apiUrl)
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Network response was not ok');
                    }
                    return response.json();
                })
                .then(data => {
                    let { leagues, teams, players, countries, trophies, stadiums } =  data
                                        
                    $(".search_recomendation").removeClass("hidden")
                    if (leagues.length) {
                        $(".leagues_datalist_ul").addClass("active")
                        
                        leagues.forEach((item) => {
                            const li = document.createElement("li");
                            li.setAttribute("title", item.name);
                            li.innerHTML = `
                                <a class="flex gap-2 w-full" href="/leagues/${item.id}/">
                                    <span class="min-w-[50px] min-h-[50px] grid place-items-center">
                                        <img width="28" height="28" src="${item.img}" />
                                    </span>
                                    <span class="whitespace-nowrap flex items-center text-sm">${enshort_name(item.name)}</span>
                                </a>
                            `;
                            $(".leagues_datalist_ul").append(li);
                        });

                        if (leagues.length == 10){
                            $(".leagues_datalist_ul").append(`<li class='text-center text-xs' style='padding: 20px 40px;'><a href='/search/leagues/${query}'>Ver todos os resultados para ligas</a></li>`)
                        }
                        

                    }else{
                        $(".leagues_datalist_ul").removeClass("content")
                        $(".leagues_datalist_ul").html("<small>Nenhuma liga encontrada</small>");
                    }

                    if (teams.length) {
                        $(".teams_datalist_ul").addClass("active")
                        teams.forEach((item) => {
                            const li = document.createElement("li");
                            li.setAttribute("title", item.name);
                            li.innerHTML = `
                                <a class="flex gap-2 w-full" href="/teams/${item.id}/">
                                    <span class="min-w-[50px] min-h-[50px] grid place-items-center">
                                        <img width="28" height="28" src="${item.img}" />
                                    </span>
                                    <span class="whitespace-nowrap flex items-center text-sm">${enshort_name(item.name)}</span>
                                </a>
                            `;
                            $(".teams_datalist_ul").append(li);
                        });
                        if (teams.length == 10){
                            $(".teams_datalist_ul").append(`<li class='text-center text-xs' style='padding: 20px 40px;'><a href='/search/teams/${query}'>Ver todos os resultados para equipes</a></li>`)
                        }


                    }else{
                        $(".teams_datalist_ul").removeClass("content")
                        $(".teams_datalist_ul").html("<small>Nenhum time encontrado</small>");
                    }

                    if (players.length) {
                        $(".players_datalist_ul").addClass("active")
                        players.forEach((item) => {
                            const li = document.createElement("li");
                            li.setAttribute("title", item.name);
                            li.innerHTML = `
                                <a class="flex gap-2 w-full items-center text-sm" href="/players/${item.id}">
                                    <span class="min-w-[50px] min-h-[50px] grid place-items-center text-sm">
                                        <img height="36" width="36" class="max-w-9 max-h-9 w-9 h-9 rounded-full object-cover" style="max-height: 36px" src="${item.img}" />
                                    </span
                                    <span class="whitespace-nowrap flex items-center text-sm">${enshort_name(item.name)}</span>
                                </a>
                            `;
                            $(".players_datalist_ul").append(li);

                        });
                        
                        if (players.length == 10){
                            $(".players_datalist_ul").append(`<li class='text-center text-xs' style='padding: 20px 40px;'><a href='/search/players/${query}'>Ver todos os resultados para jogadores</a></li>`)
                        }


                    }else{
                        $(".players_datalist_ul").removeClass("content")
                        $(".players_datalist_ul").html("<small>Nenhum jogador encontrado</small>");
                    }
                    if (countries.length) {
                        $(".countries_datalist_ul").addClass("active")
                        countries.forEach((item) => {
                            const li = document.createElement("li");
                            li.setAttribute("title", item.name);
                            li.innerHTML = `
                                <a class="flex gap-2 w-full" href="/countries/${item.id}">
                                    <span class="min-w-[50px] min-h-[50px] grid place-items-center">
                                        <img width="28" height="28" src="${item.img}" />
                                    </span>
                                    <span class="whitespace-nowrap flex items-center text-sm">${enshort_name(item.name)}</span>
                                </a>
                            `;
                            $(".countries_datalist_ul").append(li);

                        });
                        if (countries.length == 10){
                            $(".countries_datalist_ul").append(`<li class='text-center text-xs' style='padding: 20px 40px;'><a href='/search/countries/${query}'>Ver todos os resultados para países</a></li>`)

                        }


                    }else{
                        $(".countries_datalist_ul").removeClass("content")
                        $(".countries_datalist_ul").html("<small>Nenhum país encontrado</small>");
                    }

                    if (trophies.length) {
                        $(".trophies_datalist_ul").addClass("active")
                        trophies.forEach((item) => {
                            const li = document.createElement("li");
                            li.setAttribute("title", item.name);
                            li.innerHTML = `
                                <a class="flex gap-2 w-full" href="/trophies/${item.id}">
                                    <span class="min-w-[50px] min-h-[50px] grid place-items-center">
                                        <img height="28" src="${item.img}" style="max-height: 36px"  />
                                    </span>
                                    <span class="whitespace-nowrap flex items-center text-sm">${enshort_name(item.name)}</span>
                                </a>
                            `;
                            $(".trophies_datalist_ul").append(li);

                        });
                        if (trophies.length == 10){
                            $(".trophies_datalist_ul").append(`<li class='text-center text-xs' style='padding: 20px 40px;'><a href='/search/trophies/${query}'>Ver todos os resultados para taças</a></li>`)
                        }


                    }else{
                        $(".trophies_datalist_ul").removeClass("content")
                        $(".trophies_datalist_ul").html("<small>Nenhuma taça encontrada</small>");
                    }


                    if (stadiums.length) {
                        $(".stadiums_datalist_ul").addClass("active")
                        stadiums.forEach((item) => {
                            const li = document.createElement("li");
                            li.setAttribute("title", item.name);
                            let img = 'https://t4.ftcdn.net/jpg/04/17/36/11/360_F_417361125_RnrhT3Np0zB0UpeD7QlwuOoyghEGGjBX.jpg'
                            if (item.imgs){
                                img = item.imgs.split("%%")[0]
                            }
                            li.innerHTML = `
                                <a class="flex gap-2 w-full" href="/stadiums/${item.id}">
                                    <span class="min-w-[50px] min-h-[50px] grid place-items-center pl-4">
                                        <img height="28" src="${img}" style="max-height: 36px; max-width: 40px"  />
                                    </span>
                                    <span class="whitespace-nowrap flex items-center text-sm">${enshort_name(item.name)}</span>
                                </a>
                            `;
                            $(".stadiums_datalist_ul").append(li);

                        });
                        if (stadiums.length == 10){
                            $(".stadiums_datalist_ul").append(`<li class='text-center text-xs' style='padding: 20px 40px;'><a href='/search/stadiums/${query}'>Ver todos os resultados para estádios</a></li>`)
                        }


                    }else{
                        $(".trophies_datalist_ul").removeClass("content")
                        $(".trophies_datalist_ul").html("<small>Nenhuma taça encontrada</small>");
                    }
                })
                .catch(error => {
                    console.error('There was a problem with the fetch operation:', error);
                });
            $(".datalist_skeleton.skeleton-loading").fadeOut();
            $("html").addClass("overflow-hidden")
        }, 1000);
    } else {
        $(".datalist_skeleton.skeleton-loading").fadeOut();
        $("html").removeClass("overflow-hidden")
    }
});

// Function to hide search recommendation on body click
$("body").click(() => {
    $(".search_recomendation").addClass("hidden");
    $(".datalist_mobile").addClass("right-full");
    $("html").removeClass("overflow-hidden")
});

// Function to prevent hiding search recommendation on leagues data list click


$(".search-icon").click((e) => {
    e.stopPropagation();
    $(".datalist_mobile").toggleClass("right-full");
    $("html").toggleClass("overflow-hidden")
});

$(".datalist, nav input").click((e) => {
    e.stopPropagation();
});


// Initialize document
$(document).ready(() => {
    $(".skeleton-loading").fadeOut();
    $("html, body").css("opacity", "1");
});

