---
title: JWT Login test (python/flask)
layout: post
description: A login screen that interacts with Python and obtains a JWT  
type: hacks
courses: { "compsci": {week: 18 }}
---


<form action="javascript:login_user()">
    <p><label>
        User ID:
        <input type="text" name="uid" id="uid" required>
    </label></p>
    <p><label>
        Password:
        <input type="password" name="password" id="password" required>
    </label></p>
    <p>
        <button>Login</button>
    </p>
</form>

<script type="module">
    import { uri, options } from '{{site.baseurl}}/assets/js/api/config.js';

    function login_user(){
        const url = uri + '/api/users/authenticate';

        const body = {
            uid: document.getElementById("uid").value,
            password: document.getElementById("password").value,
        };

        const authOptions = {
            ...options, // This will copy all properties from options
            method: 'POST', // Override the method property
            cache: 'no-cache', // Set the cache property
            body: JSON.stringify(body)
        };

        fetch(url, authOptions)
        .then(response => {
            if (!response.ok) {
                const errorMsg = 'Login error: ' + response.status;
                console.log(errorMsg);
                return;
            }
            window.location.href = "{{site.baseurl}}/data/database";
        })
        .catch(err => {
            console.error(err);
        });
    }

    window.login_user = login_user;
</script>

