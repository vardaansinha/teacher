---
title: Itunes API
comments: true
layout: default
description: API's are a primary source for obtaining data from the internet.  There is imformation in API's for almost any interest.
permalink: /frontend/home_table
categories: [C7.0]
courses: { csse: {week: 3}, csp: {week: 0, categories: [2.C]}, csa: {week: 0} }
---


{% include nav_home.html %}

<!-- HTML table fragment for page -->
<table>
  <thead>
  <tr>
    <th>Artist</th>
    <th>Collection</th>
    <th>Images</th>
    <th>Preview</th>
  </tr>
  </thead>
  <tbody id="result">
    <!-- generated rows -->
  </tbody>
</table>

<!-- Script is layed out in a sequence (no function) and will execute when page is loaded -->
<script>
  // prepare HTML result container for new output
  const resultContainer = document.getElementById("result");

  // prepare fetch options
  const url = "https://itunes.apple.com/search?term=every+breathe+you+take";
  const headers = {
    method: 'GET', // *GET, POST, PUT, DELETE, etc.
    mode: 'cors', // no-cors, *cors, same-origin
    cache: 'default', // *default, no-cache, reload, force-cache, only-if-cached
    credentials: 'omit', // include, *same-origin, omit
    headers: {
      'Content-Type': 'application/json'
      // 'Content-Type': 'application/x-www-form-urlencoded',
    },
  };

  // fetch the API
  fetch(url, headers)
    // response is a RESTful "promise" on any successful fetch
    .then(response => {
      // check for response errors
      if (response.status !== 200) {
          const errorMsg = 'Database response error: ' + response.status;
          console.log(errorMsg);
          const tr = document.createElement("tr");
          const td = document.createElement("td");
          td.innerHTML = errorMsg;
          tr.appendChild(td);
          resultContainer.appendChild(tr);
          return;
      }
      // valid response will have json data
      response.json().then(data => {
          console.log(data);

          // Music data
          for (const row of data.results) {
            console.log(row);

            // tr for each row
            const tr = document.createElement("tr");
            // td for each column
            const artist = document.createElement("td");
            const collection = document.createElement("td");
            const image = document.createElement("td");
            const preview = document.createElement("td");

            // data is specific to the API
            artist.innerHTML = row.artistName;
            collection.innerHTML = row.collectionName; 
            // create preview image
            const img = document.createElement("img");
            img.src = row.artworkUrl100;
            image.appendChild(img);
            // create preview player
            const audio = document.createElement("audio");
            audio.controls = true;
            const source = document.createElement("source");
            source.src = row.previewUrl;
            source.type = "audio/mp4";
            audio.appendChild(source);
            preview.appendChild(audio);

            // this builds td's into tr
            tr.appendChild(artist);
            tr.appendChild(collection);
            tr.appendChild(image);
            tr.appendChild(preview);

            // add HTML to container
            resultContainer.appendChild(tr);
          }
      })
  })
  // catch fetch errors (ie ACCESS to server blocked)
  .catch(err => {
    console.error(err);
    const tr = document.createElement("tr");
    const td = document.createElement("td");
    td.innerHTML = err;
    tr.appendChild(td);
    resultContainer.appendChild(tr);
  });
</script>
