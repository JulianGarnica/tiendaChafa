<template>
  <MiddleBox class="shadowHover centerDiv">
    <v-form v-model="formValid" @submit.prevent>
      <v-container>
        <v-row>
          <v-col cols="12" md="12">
            <h1>{{ titulo }}</h1>
          </v-col>

          <v-col cols="12" md="12">
            <slot />
          </v-col>

          <v-col cols="12" md="4">
            <v-text-field
              :rules="rules"
              label="Nombre"
              v-model="formData.nombre"
              required
            ></v-text-field>
          </v-col>

          <v-col cols="12" md="4">
            <v-text-field
              :rules="rules"
              label="Correo"
              type="email"
              v-model="formData.correo"
              required
            ></v-text-field>
          </v-col>

          <v-col cols="12" md="4">
            <v-text-field
              :rules="rules"
              type="password"
              label="Contraseña"
              v-model="formData.password"
              required
            ></v-text-field>
          </v-col>


          <v-col cols="12" md="12">
            <v-btn
              color="success"
              class="mr-4"
              type="submit"
              :disabled="!formValid"
              @click="enviarDataChildren()"
            >
              Registrar
            </v-btn>

            <v-btn color="error" class="mr-4" @click="reset()" v-if="limpiar">
              Limpiar
            </v-btn>
          </v-col>
        </v-row>
      </v-container>
    </v-form>
  </MiddleBox>
</template>

<script>
import MiddleBox from "../components/static/MiddleBox.vue";

export default {
  name: "HomeView",
  components: {
    MiddleBox,
  },
  props: {
    formData: Object,
    titulo: String,
    limpiar: Boolean,
  },
  data: () => ({
    formDataDefault: {
      nombre: "",
      correo: "",
      password: ""
    },
    formValid: false,
    rules: [
      (value) => {
        if (value) return true;

        return "Este campo es obligatorio";
      },
    ],
  }),
  methods: {
    enviarDataChildren: function () {
      this.$emit("enviarData");
    },
    reset: function () {
      this.formData = this.formDataDefault
    },
  },
};
</script>

<style scoped>
.home {
  background: #fff;
}

.centerDiv {
  margin-top: 50px !important;
}
</style>
