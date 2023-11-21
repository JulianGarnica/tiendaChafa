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
              :counter="30"
              label="Nombre"
              v-model="formData.nombre"
              required
            ></v-text-field>
          </v-col>

          <v-col cols="12" md="12">
            <v-textarea
              name="input-7-1"
              v-model="formData.descripcion"
              label="Descripción"
            ></v-textarea>
          </v-col>

          <v-col cols="12" md="4">
            <v-text-field
              :rules="rules"
              label="Costo"
              type="number"
              v-model="formData.costo"
              required
            ></v-text-field>
          </v-col>

          <v-col cols="12" md="4">
            <v-text-field
              :rules="rules"
              :counter="10"
              label="Cantidad"
              type="number"
              v-model="formData.cantidad"
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
    itemsSexo: [
      "Masculino",
      "Femenino",
      "Transformer",
      "No sé",
      "Venezolano",
      "Otro",
    ],
    formDataDefault: {
      nombre: "",
      apellido: "",
      edad: "",
      sexo: "",
      correo: "",
      telefono: "",
      sistemaSalud: "",
      medicamentos: false,
      alimentos: false,
      pastillas: false,
      otros: false,
      grupoSanguineo: "",
      observaciones: "",
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
