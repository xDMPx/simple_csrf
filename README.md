# simple_csrf

This repository demonstrates a basic example of executing a Cross-Site Request Forgery (CSRF) attack on a vulnerable web application, created as part of the Web Application Security project.

## CSRF Example
`csrf_example` directory contains a Django web application simulating a simple "bank account system".

## CSRF HTML

`index.html` allows easy execution of CSRF attacks. This file also contains an HTML form that illustrates a CSRF attack on a POST request.

`csrf_html` CSRF attacks on GET: 

* `same_site_none_get.html` - example of how to attack GET when `SameSite` cookie attribute is set to `None`
* `same_site_lax_get.html` - example of how to attack GET when `SameSite` cookie attribute is set to `Lax`

## Lax
To test CSRF attack when the cookie attribute is set to `Lax`, it is necessary to modify `settings.py` as follows:
```
SESSION_COOKIE_SAMESITE = 'Lax'
```
