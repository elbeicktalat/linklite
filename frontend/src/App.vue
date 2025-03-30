<template>
  <Toaster position="top-right" />
  <div>
    <router-view />
  </div>
</template>

<script setup>
import { Toaster } from 'vue-sonner'
</script>
