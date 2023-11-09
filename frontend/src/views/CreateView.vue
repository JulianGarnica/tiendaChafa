<template>
  <div>
    <formFichaMedica
      @enviarData="enviarData"
      :formData="formData"
      titulo="Crear Ficha Médica"
      :limpiar="true"
    >
      <router-link :to="'/'">
        <v-btn class="mx-2" fab dark large color="cyan">
          <v-icon dark> mdi-keyboard-return </v-icon>
        </v-btn>
      </router-link></formFichaMedica
    >
  </div>
</template>

<script>
import MiddleBox from "../components/static/MiddleBox.vue";
import formFichaMedica from "@/components/formFichaMedica.vue";
import { insertFichaMedica } from "../api";

export default {
  name: "HomeView",
  components: {
    MiddleBox,
    formFichaMedica,
  },
  data: () => ({
    formData: {
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
  }),
  methods: {
    enviarData: function () {
      console.log(this.formData);
      insertFichaMedica(this.formData).then((response) => {
        this.$router.push("/")
      });
    },
    reset: function () {
      console.log("Limpiando");
    },
  },
};
</script>

<style scoped>
.home {
  background: #fff;
}

.centerDiv {
  margin: 0 auto;
}
</style>
