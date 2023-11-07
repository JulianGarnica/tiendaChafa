<template>
  <section>
    <input
      type="checkbox"
      v-model="mostrarMenu"
      class="expanderMenu"
      id="expanderMenu"
    />
    <div
      class="menu shadowHover"
      :class="{ menuExpandido: mostrarMenu }"

      tabindex="0"
    >
    <!-- @focusout="cerrarMenu()" -->
      <span></span>
      <div class="options">
        <div class="MenuExpanderResponsive">
          <div class="option tooltip" @click="cambiarEstadoMenu()">
            <span class="tooltiptext" v-if="!mostrarMenu">Expandir menú</span>
            <v-icon size="40px">
              {{ expandIcon }}
            </v-icon>
          </div>
        </div>

        <div class="contentMenu">
          <router-link :to="'/'">
            <div class="option tooltip">
              <span class="tooltiptext" v-if="!mostrarMenu">Inicio</span>
              <div>
                <v-icon size="40px"> mdi-home </v-icon>
                <span v-if="mostrarMenu">&nbsp;Inicio</span>
              </div>
            </div>
          </router-link>

          <div v-for="(option, key) in menuOptions" :key="key">
            <div v-if="option.hasSubmenus">
              <input type="radio" name="expander" :id="'expander-' + key" />
              <label :for="'expander-' + key">
                <div class="option tooltip" @click="abrirMenu">
                  <span class="tooltiptext" v-if="!mostrarMenu">{{
                    option.name
                  }}</span>
                  <div>
                    <v-icon size="40px">
                      {{ option.icon }}
                    </v-icon>
                    <span v-if="mostrarMenu">&nbsp;{{ option.name }}</span>
                  </div>
                </div>
              </label>

              <div v-if="mostrarMenu" class="submenu">
                <div
                  class="subopcion"
                  v-for="(subOption, key) in option.submenu"
                  :key="key"
                >
                  {{ subOption.name }}
                </div>
              </div>
            </div>

            <div v-else>
              <router-link :to="option.url">
                <div class="option tooltip">
                  <span class="tooltiptext" v-if="!mostrarMenu">{{
                    option.name
                  }}</span>
                  <div>
                    <v-icon size="40px">
                      {{ option.icon }}
                    </v-icon>
                    <span v-if="mostrarMenu">&nbsp;{{ option.name }}</span>
                  </div>
                </div>
              </router-link>
            </div>
          </div>

          <div class="bottomOptions">
            <div v-for="(option, key) in menuBottomsOptions" :key="key">
              <div v-if="option.hasSubmenus">
                <input
                  type="radio"
                  name="expander"
                  :id="'subexpander-' + key"
                />
                <label :for="'subexpander-' + key">
                  <div class="option tooltip" @click="abrirMenu">
                    <span class="tooltiptext" v-if="!mostrarMenu">{{
                      option.name
                    }}</span>
                    <div>
                      <v-icon size="40px">
                        {{ option.icon }}
                      </v-icon>
                      <span v-if="mostrarMenu">&nbsp;{{ option.name }}</span>
                    </div>
                  </div>
                </label>

                <div v-if="mostrarMenu" class="submenu">
                  <div
                    v-for="(subOption, key) in option.submenu"
                    :key="key"
                    @click="enviarOpcSubmenu(subOption.url)"
                  >
                    {{ subOption.name }}
                  </div>
                  <div v-if="option.name == 'Usuario'" @click="cerrarSesion">
                    Cerrar sesión
                  </div>
                </div>
              </div>

              <!-- <div v-else>
            <div class="option tooltip">
              <span class="tooltiptext" v-if="!mostrarMenu">{{
                option.name
              }}</span>
              <div>
                <v-icon size="40px">
                  {{ option.icon }}
                </v-icon>
                <span v-if="mostrarMenu">&nbsp;{{ option.name }}</span>
              </div>
            </div>
          </div> -->
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import { getMenu } from "@/api";

export default {
  data() {
    return {
      expandIcon: "mdi-arrow-right",
      mostrarMenu: false,
      menuOptions: [],

      menuBottomsOptions: [
        {
          icon: "mdi-account",
          name: "Usuario",
          url: "/",
          hasSubmenus: true,
          submenu: [
            {
              name: "Cambiar contraseña",
              url: "/opcionesUser",
            },
          ],
        },
        // {
        //   icon: "mdi-cog",
        //   name: "Configuración",
        //   url: "/",
        //   hasSubmenus: true,
        //   submenu: [
        //     {
        //       name: "Configuración aplicación",
        //       url: "/bodegas/",
        //     },
        //   ],
        // },
      ],
    };
  },

  methods: {
    enviarOpcSubmenu(url) {
      if (this.$route.path !== url) this.$router.push(url);
    },

    cambiarEstadoMenu() {
      this.mostrarMenu = !this.mostrarMenu;
    },

    abrirMenu() {
      this.mostrarMenu = true;
    },

    cerrarMenu() {
      this.mostrarMenu = false;
    },

    cerrarSesion() {
      localStorage.removeItem("userTkn");
      window.location.reload();
    },
  },

  mounted() {
    getMenu().then(
      function (response) {
        this.menuOptions = response.data;
      }.bind(this)
    );
  },

  watch: {
    mostrarMenu(newState) {
      if (newState) {
        this.expandIcon = "mdi-arrow-left";
      } else {
        this.expandIcon = "mdi-arrow-right";
      }
    },
    $route (to, from){
      this.mostrarMenu = false;
    }

  },
};
</script>

<style scoped>
.menu {
  position: fixed;
  display: grid;
  grid-template-rows: auto 1fr auto;
  height: 100%;
  width: 90px;
  z-index: 100;
  background-color: #385da6;
  color: #fff;
  overflow-x: hidden;
  transition: 0.4s;
  padding: 1rem 0;
  box-sizing: border-box;
}

.menu a {
  color: #fff;
}

i.v-icon.v-icon {
  color: #fff;
}
.menuExpandido {
  width: 300px !important;
  text-align: left;
  margin: 0px !important;
}
.menuExpandido .option {
  padding-left: 30px;
  margin: 5px;
  margin-left: 30px;
}

.menuExpandido .submenu div {
  padding: 10px;
  margin: 10px;
  padding-left: 60px;
  list-style: none;
  cursor: pointer;
  transition: 0.3s;
}

hr {
  width: 80%;
  border: 2px solid #2c3e50;
  border-radius: 5px;
  margin: auto;
}
.menuExpandido .submenu div:hover {
  border-radius: 30px;
  background-color: #0b2559;
  color: white;
  box-shadow: rgba(0, 0, 0, 0.1) 0px 0px 5px 0px,
    rgba(0, 0, 0, 0.1) 0px 0px 1px 0px;
}

.menu .option {
  padding-top: 10px;
  padding-bottom: 10px;
  margin: 10px;
  cursor: pointer;
  transition: 0.3s;
}

.menu .option:hover {
  border-radius: 30px;
  background-color: #0b2559;
  color: white;
  box-shadow: rgba(0, 0, 0, 0.1) 0px 0px 5px 0px,
    rgba(0, 0, 0, 0.1) 0px 0px 1px 0px;
}

.menu .options {
  height: 80%;
}

.menu .bottomOptions {
  height: 10%;
}

.expanderMenu {
  display: none;
}

.tooltip .tooltiptext {
  visibility: hidden;
  width: 120px;
  left: 95px;
  background-color: black;
  color: #fff;
  text-align: center;
  border-radius: 6px;
  padding: 5px 0;
  transition: 0.3s;
  opacity: 0;

  /* Position the tooltip */
  position: fixed;
  z-index: 1;
}

.tooltip:hover .tooltiptext {
  opacity: 1;
  visibility: visible;
}
input[name="expander"] {
  display: none;
}

.submenu {
  text-decoration: none;

  text-align: left;
}
.contentMenu {}

input[type="radio"]:not(:checked) ~ div {
  animation: close 1.5s;
  display: none;
  height: 0;
  max-height: 500px;
}

input[type="radio"]:checked ~ div {
  animation: open 1.5s;
  display: block;
  height: auto;
  max-height: 500px;
}

@keyframes open {
  from {
    max-height: 0;
    display: block;
    opacity: 0;
  }
  to {
    max-height: auto;
    opacity: 1;
  }
}

@keyframes close {
  from {
    max-height: 500px;
    opacity: 1;
  }
  to {
    display: none;
    max-height: 0;
    opacity: 0;
  }
}

@media (max-width: 600px) {
  #expanderMenu:not(:checked) ~ .menu {
    height: 80px !important;
    border-radius: 100px !important;
    margin: 10px;
    padding: 0rem 0;
  }

  #expanderMenu:not(:checked) ~ .contentMenu {
    display: none !important;
  }

  #expanderMenu:checked ~ .menu {
    position: fixed;
    display: grid;
    grid-template-rows: auto 1fr auto;
    height: 100%;
    width: 90px;
    z-index: 100;
    background-color: #385da6;
    color: #fff;
    overflow-x: hidden;
    transition: 0.4s;
    padding: 1rem 0;
    box-sizing: border-box;
  }

  #expanderMenu:checked ~ * .contentMenu {
    display: contents;
  }

  .MenuExpanderResponsive {
  }

  .contentMenu{
    display: none;
  }
}
</style>
