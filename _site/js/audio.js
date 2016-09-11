// ***************************************** //
// audio.js javascript file for music player //
// Simple version 2016-09-11                 // 
// ***************************************** //

// Global Variables
var playlist = [];      //NodeList storing all songs

// Initialize variables after <audio> elements have loaded
window.onload = function() {
    //load all elements with class "song" into playlist
    playlist = document.getElementsByClassName("song");

    //add events to play next song when previous ends
    for (var j = 0; j < playlist.length; j++) {
        let item = playlist[j];
        document.getElementById(item.id).onended = function() {
            //id contains track number of song
            var next = parseInt(item.id,10) + 1;
            document.getElementById(next).play();
        }
   }
}
