<template>
  <div class="mx-auto my-12 ">
    <div class="logoEmpresaLogin shadowHover">
      <v-img width="100%" src="@/assets/logo.png"></v-img>
    </div>

    <v-card :loading="loading" width="374" outlined class="cardLogin shadowHover">
      <template slot="progress">
        <v-progress-linear
          color="deep-purple"
          height="4"
          indeterminate
        ></v-progress-linear>
      </template>

      <v-card-title class="titulo text-center">Recuperar contraseña</v-card-title>

      <v-card-text>
        <v-form ref="form" v-model="valid" lazy-validation>
          Ingrese su correo y si es válido, va a recibir una notificación con su nueva contraseña.
          <v-container>
            <v-row>
              <v-col cols="12" md="12">
                <v-text-field
                  v-model="user"
                  label="Correo"
                  :rules="rulesRequired"
                  required
                ></v-text-field>
              </v-col>

            </v-row>
          </v-container>
        </v-form>
      </v-card-text>

      <v-divider class="mx-4"></v-divider>

      <v-card-actions>
        <v-row>
          <v-col cols="12" md="12">
            <v-btn color="lighten-2" text @click="actualizarPassword">
              Cambiar contraseña
            </v-btn>
          </v-col>
          <v-col cols="12" md="6">
            <v-btn color="lighten-2" text @click="iniciarSesion">
              Iniciar sesión
            </v-btn>
          </v-col>
          <v-col cols="12" md="6">
            <v-btn color="lighten-2" text @click="registerHelp">
              ¿Desea <br />
              registrarse?
            </v-btn>
          </v-col>
        </v-row>
      </v-card-actions>

      <v-alert
        :value="alertError"
        color="error"
        dark
        border="top"
        icon="mdi-error"
        transition="slide-y-transition"
        style="z-index:1"
      >
        <div class="pt-2 pr-6">
          <v-btn color="error" fab x-small @click="show_alert_and_fade">
            <v-icon>mdi-close</v-icon>
          </v-btn>

          <br /><br />
          {{ msgError }}
        </div>
      </v-alert>

      <v-alert
        :value="alert"
        color="lighten-2"
        dark
        border="top"
        icon="mdi-error"
        transition="slide-y-transition"
        style="z-index:1"
      >
        <div class="pt-2 pr-6">
          <v-btn color="lighten-2" fab x-small @click="show_alert_and_fade">
            <v-icon>mdi-close</v-icon>
          </v-btn>

          <br /><br />
          {{ msgAlert }}
        </div>
      </v-alert>
    </v-card>
  </div>
</template>

<script>
import { changePassword } from "@/api/";

export default {
  data: () => ({
    loading: false,
    valid: true,
    selection: 1,
    user: null,
    password: null,
    rulesRequired: [(v) => !!v || "Este campo es obligatorio"],
    msgError: "",
    alertError: false,
    alert: false,
    msgAlert: ""
  }),

  methods: {
    actualizarPassword() {
      const validateForm = this.$refs.form.validate();
      if (validateForm) {
        this.loading = true;
        this.alertError = false;
        changePassword({
          user: this.user,
        })
          .then(
            function (response) {
              if (response.data[0].status == 1) {
                this.loading = false;
                this.alert = true;
                this.msgAlert =
                  "Proceso realizado con éxito. Si el correo es correcto, va a recibir un correo con la nueva contraseña.";
              } else {
                this.loading = false;
                this.alertError = true;
                this.msgError =
                  "Error de comunicación, comuníquese con el administrador.";
              }
            }.bind(this)
          )
          .catch(
            function (error) {
              this.loading = false;
              this.alertError = true;
              this.msgError =
                "Error al realizar solicitud, contáctese con el administrador.";
            }.bind(this)
          );
      }
    },

    registerHelp(){},

    iniciarSesion(){
      this.$router.push({ path: '/'}).catch(()=>{});
    },

    show_alert_and_fade() {
      this.alertError = !this.alertError;
    },
  },
};
</script>

<style>
.logoEmpresaLogin {
  position: absolute;
  width: 374px;
  background-color: #fff;
  padding: 20px;
  border-radius: 90px;
  z-index: 1;
}

.cardLogin {
  margin-top: 130px;
  border: 0 !important;
  border-radius: 10px !important;
  padding-top: 30px;
}

.cardLogin .titulo {
  display: block !important;
}
</style>
