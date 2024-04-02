// Function to toggle menu
$(".toggle-menu").click(() => {
    $("body").toggleClass("menu-active");
});

// Function to show search recommendations when input field is focused
$(".search_field input").focus(() => {
    $(".search_recomendation").removeClass("hidden");
});

// Function to convert string to slug
function slugify(str) {
    // Remove leading and trailing whitespace
    str = str.replace(/^\s+|\s+$/g, '');
    // Convert to lowercase
    str = str.toLowerCase();
    // Define special characters and their replacements
    const from = "àãáäâèéëêìíïîòóöõôùúüûñç·/_,:;";
    const to = "aaaaaeeeeiiiioooouuuunc------";
    // Replace special characters
    for (let i = 0, l = from.length; i < l; i++) {
        str = str.replace(new RegExp(from.charAt(i), 'g'), to.charAt(i));
    }
    // Remove special characters
    str = str.replace(/[^a-z0-9 -]/g, '')
             // Replace spaces with hyphens
             .replace(/\s+/g, '-')
             // Remove multiple hyphens
             .replace(/-+/g, '-');
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
    $(".datalist_ul").removeClass("active");

    clearTimeout(typingTimer);
    if (e.target.value) {
        $(".datalist_skeleton.skeleton-loading").fadeIn();
        $("html").addClass("overflow-hidden");

        typingTimer = setTimeout(() => {
            const query = slugify(e.target.value.trim());
            const apiUrl = `/search_items/${query}/`;

            fetch(apiUrl)
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Network response was not ok');
                    }
                    return response.json();
                })
                .then(data => {
                    // Process search results
                    let { leagues, teams, players, countries, trophies, stadiums } = data;

                    // Display leagues
                    if (leagues.length) {
                        $(".search_recomendation").removeClass("hidden");
                        $(".leagues_datalist_ul").addClass("active");
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
                        if (leagues.length == 10) {
                            $(".leagues_datalist_ul").append(`<li class='text-center text-xs' style='padding: 20px 40px;'><a href='/search/leagues/${query}'>Ver todos os resultados para ligas</a></li>`);
                        }
                    } else {
                        $(".leagues_datalist_ul").removeClass("content");
                        $(".leagues_datalist_ul").html("<small>Nenhuma liga encontrada</small>");
                    }

                    // Display teams, players, countries, trophies, stadiums (similar logic)

                })
                .catch(error => {
                    console.error('There was a problem with the fetch operation:', error);
                });
            $(".datalist_skeleton.skeleton-loading").fadeOut();
            $("html").addClass("overflow-hidden");
        }, 1000);
    } else {
        $(".datalist_skeleton.skeleton-loading").fadeOut();
        $("html").removeClass("overflow-hidden");
    }
});

// Function to hide search recommendation on body click
$("body").click(() => {
    $(".search_recomendation").addClass("hidden");
    $(".datalist_mobile").addClass("right-full");
    $("html").removeClass("overflow-hidden");
});

// Function to prevent hiding search recommendation on leagues data list click
$(".search-icon").click((e) => {
    e.stopPropagation();
    $(".datalist_mobile").toggleClass("right-full");
    $("html").toggleClass("overflow-hidden");
});

$(".datalist, nav input").click((e) => {
    e.stopPropagation();
});

// Initialize document
$(document).ready(() => {
    $(".skeleton-loading").fadeOut();
    $("html, body").css("opacity", "1");
});
