d3.json('https://jsonplaceholder.typicode.com/posts', {
      method:"POST",
      body: JSON.stringify({
        title: 'Hello',
        body: '_d3-fetch_ is it',
        userId: 1,
        friends: [2,3,4]
      }),
      headers: {
        "Content-type": "application/json; charset=UTF-8"
      }
    })
    .then(json => {
     // do something with the response --> put the response into your page
    });