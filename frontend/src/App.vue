<template>
  <v-app v-if="validUser">
    <div class="content">
      <FullBoxVue class="shadowHover" v-show="loading">
        <loadingCSS> Cargando... </loadingCSS>
      </FullBoxVue>
      <v-btn class="mx-2" dark large color="cyan" @click="cerrarSesion()">
        Cerrar sesión
      </v-btn>
      <router-view v-show="!loading" v-slot="{ Component }">
        <transition name="fade">
          <component :is="Component" />
        </transition>
      </router-view>
    </div>
    <p style="display: none">Versión 1.1</p>
  </v-app>

  <v-app v-else-if="$route.matched[0].path == '/candidatoUpload/:id'">
    <router-view v-show="!loading" v-slot="{ Component }">
      <transition name="fade">
        <component :is="Component" />
      </transition>
    </router-view>
    <FullBoxVue class="shadowHover" v-show="loading">
      <v-img
        :src="require('./assets/logo.png')"
        class="my-3"
        contain
        height="100"
      />
      <loadingCSS> Cargando... </loadingCSS>
    </FullBoxVue>
    <p style="display: none">Versión 1.1</p>
  </v-app>
  <v-app v-else-if="$route.matched[0].path == '/restorePassword'">
    <RestorePassword v-show="!loading"></RestorePassword>
    <FullBoxVue class="shadowHover" v-show="loading">
      <v-img
        :src="require('./assets/logo.png')"
        class="my-3"
        contain
        height="100"
      />
      <loadingCSS> Cargando... </loadingCSS>
    </FullBoxVue>
    <p style="display: none">Versión 1.1</p>
  </v-app>
  <v-app class="NoMenuContent" v-else>
    <Login class="Login" />

    <svg
      xmlns="http://www.w3.org/2000/svg"
      class="svgBackground"
      viewBox="0 0 1440 320"
    >
      <path
        fill="#385DA6"
        fill-opacity="1"
        d="M0,64L48,101.3C96,139,192,213,288,224C384,235,480,181,576,149.3C672,117,768,107,864,133.3C960,160,1056,224,1152,234.7C1248,245,1344,203,1392,181.3L1440,160L1440,320L1392,320C1344,320,1248,320,1152,320C1056,320,960,320,864,320C768,320,672,320,576,320C480,320,384,320,288,320C192,320,96,320,48,320L0,320Z"
      ></path>
    </svg>
    <p style="display: none">Versión 1.1</p>
  </v-app>
</template>

<script>
import FullBoxVue from "./components/static/FullBox.vue";
import Login from "./components/static/Login.vue";
import RestorePassword from "./components/static/RestorePassword.vue";
import Menu from "./components/static/Menu.vue";
import { infoUser } from "./api";
import axios from "axios";
import loadingCSS from "./components/static/loadingCSS.vue";
import packageJson from "../package.json";

export default {
  name: "App",
  data: () => ({
    validUser: false,
    loading: false,
  }),
  components: {
    Menu,
    Login,
    RestorePassword,
    loadingCSS,
    FullBoxVue,
  },
  methods: {
    validLogin() {
      if (localStorage.getItem("userTkn") === null) {
        this.validUser = false;
      } else {
        this.validUser = true;
      }
    },
    cerrarSesion() {
      localStorage.removeItem("userTkn")
      window.location.reload();
    }
  },
  mounted: function () {
    this.validLogin();
    const appVersion = packageJson.version;
    if (appVersion !== localStorage.getItem("appVersion")) {
      localStorage.setItem("appVersion", appVersion);
      window.location.reload();
    }
  },

  watch: {
    $route() {
      this.$nextTick(this.validLogin);
    },
  },
  created() {
    axios.interceptors.request.use(
      (config) => {
        this.loading = true;
        return config;
      },
      (error) => {
        this.loading = false;
        return Promise.reject(error);
      }
    );

    axios.interceptors.response.use(
      (response) => {
        this.loading = false;
        return response;
      },
      (error) => {
        this.loading = false;
        return Promise.reject(error);
      }
    );
  },
};
</script>


<style>
@import url("https://fonts.googleapis.com/css2?family=Lato:wght@700&display=swap");
*::-webkit-scrollbar {
  width: 0.5em;
}
*::-webkit-scrollbar-track {
  box-shadow: inset 0 0 2px rgba(0, 0, 0, 0.3);
}
*::-webkit-scrollbar-thumb {
  background-color: darkgrey;
  outline: 1px solid slategrey;
}
body {
  background-color: #d4ceff;
  font-size: 1rem !important;
}
.shadowHover {
  box-shadow: rgba(0, 0, 0, 0.14) 0px 3px 8px;
  transition: 0.4s;
}
.shadowHover:hover {
  box-shadow: rgba(0, 0, 0, 0.3) 0px 3px 8px;
  transition: 0.4s;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  background-color: #d4ceff;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='100%25' height='100%25' viewBox='0 0 1600 800'%3E%3Cg %3E%3Cpath fill='%23ddd8ff' d='M486 705.8c-109.3-21.8-223.4-32.2-335.3-19.4C99.5 692.1 49 703 0 719.8V800h843.8c-115.9-33.2-230.8-68.1-347.6-92.2C492.8 707.1 489.4 706.5 486 705.8z'/%3E%3Cpath fill='%23e6e1ff' d='M1600 0H0v719.8c49-16.8 99.5-27.8 150.7-33.5c111.9-12.7 226-2.4 335.3 19.4c3.4 0.7 6.8 1.4 10.2 2c116.8 24 231.7 59 347.6 92.2H1600V0z'/%3E%3Cpath fill='%23eeebff' d='M478.4 581c3.2 0.8 6.4 1.7 9.5 2.5c196.2 52.5 388.7 133.5 593.5 176.6c174.2 36.6 349.5 29.2 518.6-10.2V0H0v574.9c52.3-17.6 106.5-27.7 161.1-30.9C268.4 537.4 375.7 554.2 478.4 581z'/%3E%3Cpath fill='%23f7f5ff' d='M0 0v429.4c55.6-18.4 113.5-27.3 171.4-27.7c102.8-0.8 203.2 22.7 299.3 54.5c3 1 5.9 2 8.9 3c183.6 62 365.7 146.1 562.4 192.1c186.7 43.7 376.3 34.4 557.9-12.6V0H0z'/%3E%3Cpath fill='%23FFFFFF' d='M181.8 259.4c98.2 6 191.9 35.2 281.3 72.1c2.8 1.1 5.5 2.3 8.3 3.4c171 71.6 342.7 158.5 531.3 207.7c198.8 51.8 403.4 40.8 597.3-14.8V0H0v283.2C59 263.6 120.6 255.7 181.8 259.4z'/%3E%3Cpath fill='%23ffffff' d='M1600 0H0v136.3c62.3-20.9 127.7-27.5 192.2-19.2c93.6 12.1 180.5 47.7 263.3 89.6c2.6 1.3 5.1 2.6 7.7 3.9c158.4 81.1 319.7 170.9 500.3 223.2c210.5 61 430.8 49 636.6-16.6V0z'/%3E%3Cpath fill='%23ffffff' d='M454.9 86.3C600.7 177 751.6 269.3 924.1 325c208.6 67.4 431.3 60.8 637.9-5.3c12.8-4.1 25.4-8.4 38.1-12.9V0H288.1c56 21.3 108.7 50.6 159.7 82C450.2 83.4 452.5 84.9 454.9 86.3z'/%3E%3Cpath fill='%23ffffff' d='M1600 0H498c118.1 85.8 243.5 164.5 386.8 216.2c191.8 69.2 400 74.7 595 21.1c40.8-11.2 81.1-25.2 120.3-41.7V0z'/%3E%3Cpath fill='%23ffffff' d='M1397.5 154.8c47.2-10.6 93.6-25.3 138.6-43.8c21.7-8.9 43-18.8 63.9-29.5V0H643.4c62.9 41.7 129.7 78.2 202.1 107.4C1020.4 178.1 1214.2 196.1 1397.5 154.8z'/%3E%3Cpath fill='%23FFFFFF' d='M1315.3 72.4c75.3-12.6 148.9-37.1 216.8-72.4h-723C966.8 71 1144.7 101 1315.3 72.4z'/%3E%3C/g%3E%3C/svg%3E");
  background-repeat: no-repeat;
  background-attachment: fixed;
  background-size: cover;
  z-index: 1;

}
.Login {
  z-index: 1;
}
.content {
  display: flex;
  justify-content: space-between;
  align-items: center;
  z-index: 1;
}
.svgBackground {
  position: absolute;
  bottom: 0;
}
a {
  text-decoration: none;
}
nav {
  padding: 30px;
}
nav a {
  font-weight: bold;
  color: #2c3e50;
}
nav a.router-link-exact-active {
  color: #42b983;
}
@media (max-width: 600px) {
  .content {
    margin-left: 0px;
  }
}
h1 {
  font-family: "Lato", sans-serif;
  font-size: 40px !important;
}
h2 {
  font-family: "Lato", sans-serif;
  font-size: 20px !important;
}
input[input] {
  border-radius: 20px;
}
.btnLong {
  width: 70%;
  margin: 10px;
  padding: 10px;
  border-radius: 30px;
  background-color: #0b2559;
  color: #fff;
  transition: 0.3s;
}
.btnLong:hover {
  background: #2c3e50;
  color: white;
  box-shadow: rgba(0, 0, 0, 0.1) 0px 0px 5px 0px,
    rgba(0, 0, 0, 0.1) 0px 0px 1px 0px;
}
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.2s ease;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

</style>
