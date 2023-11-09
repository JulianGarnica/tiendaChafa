<template>
  <div>
    <formFichaMedica
      @enviarData="enviarData"
      :formData="formData"
      titulo="Actualizar Ficha Médica"
      :limpiar="false"
    >
      <router-link :to="'/'">
        <v-btn class="mx-2" fab dark large color="cyan">
          <v-icon dark> mdi-keyboard-return </v-icon>
        </v-btn>
      </router-link>
    </formFichaMedica>
  </div>
</template>

<script>
import MiddleBox from "../components/static/MiddleBox.vue";
import formFichaMedica from "@/components/formFichaMedica.vue";
import { getFichaMedica, updateFichaMedica } from "../api";

export default {
  name: "HomeView",
  components: {
    MiddleBox,
    formFichaMedica,
  },
  data() {
    return {
      idSolicitud: this.$route.params.id,
      formData: {
        id: this.$route.params.id,
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
    };
  },
  methods: {
    getData: function () {
      getFichaMedica(this.idSolicitud).then((response) => {
        this.formData = response.data[0];
      });
    },
    enviarData: function () {
      updateFichaMedica(this.formData).then((response) => {});
    },
  },
  mounted() {
    this.getData();
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
