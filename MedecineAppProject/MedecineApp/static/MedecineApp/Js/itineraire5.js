async function initMap(cas,orig,destin) {

    
    const map = new google.maps.Map(cas.querySelector(".map") , {
        center: { lat: 48.8566, lng: 2.3522 },  // Coordonnées de Paris
        zoom: 8,
    });
    
    const directionsService = new google.maps.DirectionsService();
    const directionsRenderer = new google.maps.DirectionsRenderer();
    directionsRenderer.setMap(map);
    
    const request = {
        origin: orig,
        destination: destin,
        travelMode: google.maps.TravelMode.DRIVING
    };
    
    directionsService.route(request, function(result, status) {
        if (status == 'OK') {
            directionsRenderer.setDirections(result);
        }
    });
}


let origine = document.querySelector("#id_emplacement").nodeValue
const Cas = document.querySelectorAll(".news-cardr")

for (const cas of Cas){
    let destination = cas.querySelector(".pharma").nodeValue

    const button = cas.querySelector(".itineraire")

    button.onclick = initMap(cas,origine,destination)
}