$(document).ready(function () {
//    let socket = new WebSocket(`ws://127.0.0.1:8000/?session_key=${sessionKey}`);
    var socket = new WebSocket(
        'ws://' + window.location.host +
        '/ws/' + CurrentUser + '/');
  
    socket.onmessage = function (e) {
        var data = JSON.parse(e.data);
        for (var key in data) {
            document.getElementById(key).innerHTML = data[key];
        }
        if (data.temp_value >= 20 && data.temp_value <= 30) {
            if (temp.classList.contains("notice_notfine")) {
                temp.classList.remove("notice_notfine")
            }
            temp.classList.add("notice_fine")
        } else {
            if (temp.classList.contains("notice_fine")) {
                temp.classList.remove(("notice_fine"))
            }
            temp.classList.add("notice_notfine")
        }
        // salinity
        if (data.salinity_value >= 5 && data.salinity_value <= 25) {
            if (salinity.classList.contains("notice_notfine")) {
                salinity.classList.remove("notice_notfine")
            }
            salinity.classList.add("notice_fine")
        } else {
            if (salinity.classList.contains("notice_fine")) {
                salinity.classList.remove(("notice_fine"))
            }
            salinity.classList.add("notice_notfine")
        }
        //pH
        if (data.pH_value >= 7.5 && data.pH_value <= 8.5) {
            if (pH.classList.contains("notice_notfine")) {
                pH.classList.remove("notice_notfine")
            }
            pH.classList.add("notice_fine")
        } else {
            if (pH.classList.contains("notice_fine")) {
                pH.classList.remove(("notice_fine"))
            }
            pH.classList.add("notice_notfine")
        }
        //alkalinity
        if (data.alkalinity_value >= 100 && data.alkalinity_value <= 150) {
            if (alkalinity.classList.contains("notice_notfine")) {
                alkalinity.classList.remove("notice_notfine")
            }
            alkalinity.classList.add("notice_fine")
        } else {
            if (alkalinity.classList.contains("notice_fine")) {
                alkalinity.classList.remove(("notice_fine"))
            }
            alkalinity.classList.add("notice_notfine")
        }
        //oxygen
        if (data.oxygen_value >= 5) {
            if (oxygen.classList.contains("notice_notfine")) {
                oxygen.classList.remove("notice_notfine")
            }
            oxygen.classList.add("notice_fine")
        } else {
            if (oxygen.classList.contains("notice_fine")) {
                oxygen.classList.remove(("notice_fine"))
            }
            oxygen.classList.add("notice_notfine")
        }
        //hydrogen_sulfide
        if (data.hydrogen_sulfide_value <= 0.03) {
            if (hydrogen_sulfide.classList.contains("notice_notfine")) {
                hydrogen_sulfide.classList.remove("notice_notfine")
            }
            hydrogen_sulfide.classList.add("notice_fine")
        } else {
            if (hydrogen_sulfide.classList.contains("notice_fine")) {
                hydrogen_sulfide.classList.remove(("notice_fine"))
            }
            hydrogen_sulfide.classList.add("notice_notfine")
        }
        //amonia
        if (data.amonia_value <= 0.01) {
            if (amonia.classList.contains("notice_notfine")) {
                amonia.classList.remove("notice_notfine")
            }
            amonia.classList.add("notice_fine")
        } else {
            if (amonia.classList.contains("notice_fine")) {
                amonia.classList.remove(("notice_fine"))
            }
            amonia.classList.add("notice_notfine")
        }
        //nitrit
        if (data.nitrit_value <= 0.2) {
            if (nitrit.classList.contains("notice_notfine")) {
                nitrit.classList.remove("notice_notfine")
            }
            nitrit.classList.add("notice_fine")
        } else {
            if (nitrit.classList.contains("notice_fine")) {
                nitrit.classList.remove(("notice_fine"))
            }
            nitrit.classList.add("notice_notfine")
        }
    };
});
