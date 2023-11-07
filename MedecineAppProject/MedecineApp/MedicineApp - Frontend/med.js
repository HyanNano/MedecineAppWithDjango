
document.addEventListener("DOMContentLoaded", function () {
    const searchBar = document.querySelector("input[type='text']");
    const newscard = document.querySelectorAll(".news-card");

    searchBar.addEventListener("input", function () {
        const searchTerm = searchBar.value.toLowerCase();

        newscard.forEach((article) => {
            const title = article.querySelector("h2").textContent.toLowerCase();
            const content = article.querySelector("p").textContent.toLowerCase();

            if (title.includes(searchTerm) || content.includes(searchTerm)) {
                article.style.display = "block";
            } else {
                article.style.display = "none";
            }
        });
    });
});