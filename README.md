# Our Website

* [Fooridise](http://fooridise.com)

------------------------------------------------------------

## Built With

* [VueJS](https://vuejs.org) -Javascript library to make reactive and responsive websites
* [Bootstrap](https://getbootstrap.com) - To build our template
* [Flask](https://flask.palletsprojects.com/en/1.1.x/) - Used to serve as REST API server to communicate our model and front-end
* [Gunicorn](https://gunicorn.org) - Used to handle our HTTP server
* [NGINX](https://nginx.org/en/) - Used to handle out HTTP proxy server


------------------------------------------------------------------------

# Deploy on your computer

## Instalation
Install miniconda3 in your system
https://docs.conda.io/en/latest/miniconda.html

Then create new environment

```
conda create -f UI.yml
```

Activate the environment
```
conda activate UI
```
---------------------------------------
## Deployment

```
gunicorn --bind 0.0.0.0:5000 app:app
```

---------------------------------------

## Contributors

* [Luis Chumpitaz](https://github.com/luisdiaz1997) - Team Lead, Front End Development, UI/UX designer
* [Christian Melendez](https://github.com/cmelendez96) - Front End Development, UI/UX designer
* [Abraham Zepeda](https://github.com/abezepeda) - Front End Development, UI/UX designer
* [Gian Carlo L. Baldonado](https://github.com/gianclbal) - Front End Development, UI/UX designer
* [Kevin Venegas](https://github.com/Kevinv234) - Github Master
