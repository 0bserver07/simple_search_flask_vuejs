# front-board

Project Layoyt:

```
.
├── README.md
├── babel.config.js (compile config)
├── node_modules (only local)
├── package-lock.json (if you get errors, just delete this)
├── package.json (package / app config)
├── public (static files)
└── src (main dish)

src:

.
├── App.vue (App skeleton)
├── assets (css)
├── components (all the dynamic components that gets reused)
├── main.js (main file to put it all together)
├── router (router file)
├── store (not used currently, important for token / auth)
└── views (Pages / Views, more static rather than dynamic component)

```

## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Lints and fixes files
```
npm run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).
