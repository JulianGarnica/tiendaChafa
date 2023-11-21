<template>
  <div>
    <formUser
      @enviarData="enviarData"
      :formData="formData"
      titulo="Actualizar Usuario"
      :limpiar="false"
    >
      <router-link :to="'/usuarios'">
        <v-btn class="mx-2" fab dark large color="cyan">
          <v-icon dark> mdi-keyboard-return </v-icon>
        </v-btn>
      </router-link>
    </formUser>
  </div>
</template>

<script>
import FullBoxVue from "../components/static/FullBox.vue";
import formUser from "@/components/formUser.vue";
import { getUsuario, updateUser } from "../api";

export default {
  name: "HomeView",
  components: {
    FullBoxVue,
    formUser,
  },
  data() {
    return {
      idSolicitud: this.$route.params.id,
      formData: {
        id: this.$route.params.id,
        nombre: "",
        correo: ""
      },
    };
  },
  methods: {
    getData: function () {
      getUsuario(this.idSolicitud).then((response) => {
        this.formData = response.data[0];
      });
    },
    enviarData: function () {
      updateUser(this.formData).then((response) => {});
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
