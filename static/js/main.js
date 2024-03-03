// Function to toggle menu
$(".toggle-menu").click(() => {
    $("body").toggleClass("menu-active");

    if ($("body").hasClass("menu-active")) {
        localStorage.setItem("isMenuOpen", true);
    } else {
        localStorage.removeItem("isMenuOpen");
    }

    $("aside, main").addClass("transition-primary");
});


$(".search_field input").focus(() => {
    $(".search_recomendation").removeClass("hidden");
});


function slugify(str) {
    str = str.replace(/^\s+|\s+$/g, ''); // Remove espaços em branco do início e do final da string
    str = str.toLowerCase(); // Converte a string para minúsculas
    const from = "àáäâèéëêìíïîòóöôùúüûñç·/_,:;";
    const to   = "aaaaeeeeiiiioooouuuunc------"; // Substituições de caracteres especiais
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
    $(".data_list_ul").html("");
    $(".data_list_ul").removeClass("active")

    clearTimeout(typingTimer);
    if (e.target.value) {
        $(".datalist_skeleton.skeleton-loading").fadeIn();

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
                    let { leagues } =  data
                    let { teams } =  data
                    let { players } =  data
                    let { countries } =  data
                    console.log(data)
                    if (leagues.length) {
                        $(".leagues_data_list_ul").addClass("active")
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
                            $(".leagues_data_list_ul").append(li);

                        });
                    }else{
                        $(".leagues_data_list_ul").removeClass("content")
                        $(".leagues_data_list_ul").html("<small>Nenhuma liga encontrada</small>");
                    }

                    if (teams.length) {
                        $(".teams_data_list_ul").addClass("active")
                        teams.forEach((item) => {
                            const li = document.createElement("li");
                            li.setAttribute("title", item.name);
                            li.innerHTML = `
                                <a class="flex gap-2 w-full" href="/teams/${item.id}/">
                                    <span class="min-w-[50px] min-h-[50px] grid place-items-center">
                                        <img width="28" height="28" src="/static/images/teams/${slugify(item.name)}${item.id}.png" />
                                    </span>
                                    <span class="whitespace-nowrap flex items-center text-sm">${enshort_name(item.name)}</span>
                                </a>
                            `;
                            $(".teams_data_list_ul").append(li);

                        });
                    }else{
                        $(".teams_data_list_ul").removeClass("content")
                        $(".teams_data_list_ul").html("<small>Nenhum time encontrado</small>");
                    }

                    if (players.length) {
                        $(".players_data_list_ul").addClass("active")
                        players.forEach((item) => {
                            const li = document.createElement("li");
                            li.setAttribute("title", item.name);
                            li.innerHTML = `
                                <a class="flex gap-2 w-full" href="#">
                                    <span class="min-w-[50px] min-h-[50px] grid place-items-center">
                                        <img width="28" height="28" src="${item.img}" />
                                    </span>
                                    <span class="whitespace-nowrap flex items-center text-sm">${enshort_name(item.name)}</span>
                                </a>
                            `;
                            $(".players_data_list_ul").append(li);

                        });
                    }else{
                        $(".players_data_list_ul").removeClass("content")
                        $(".players_data_list_ul").html("<small>Nenhum jogador encontrado</small>");
                    }
                    if (countries.length) {
                        $(".countries_data_list_ul").addClass("active")
                        countries.forEach((item) => {
                            const li = document.createElement("li");
                            li.setAttribute("title", item.name);
                            li.innerHTML = `
                                <a class="flex gap-2 w-full" href="/country/${item.id}">
                                    <span class="min-w-[50px] min-h-[50px] grid place-items-center">
                                        <img width="28" height="28" src="${item.img}" />
                                    </span>
                                    <span class="whitespace-nowrap flex items-center text-sm">${enshort_name(item.name)}</span>
                                </a>
                            `;
                            $(".countries_data_list_ul").append(li);

                        });
                    }else{
                        $(".countries_data_list_ul").removeClass("content")
                        $(".countries_data_list_ul").html("<small>Nenhum país encontrado</small>");
                    }

                })
                .catch(error => {
                    console.error('There was a problem with the fetch operation:', error);
                });
            $(".datalist_skeleton.skeleton-loading").fadeOut();
        }, 2000);
    } else {
        $(".datalist_skeleton.skeleton-loading").fadeOut();
    }
});

// Function to hide search recommendation on body click
$("body").click(() => {
    $(".search_recomendation").addClass("hidden");
});

// Function to prevent hiding search recommendation on leagues data list click
$(".leagues_data_list").click((e) => {
    e.stopPropagation();
    $(".search_recomendation").removeClass("hidden");
});

// Initialize document
$(document).ready(() => {
    $(".skeleton-loading").fadeOut();
    if (localStorage.getItem("isMenuOpen")) {
        $("body").addClass("menu-active");
    }
    $("html, body").css("opacity", "1");
});
