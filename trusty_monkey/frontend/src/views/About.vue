<template>
<div>
  <h1>Hello World!!!!!</h1>
  <p>{{ id }}</p>
  </div>
</template>


<script>

export default {
  name: "Question",
  props: {
    id: {
      type: String,
      required: true
    }
  },
}
</script>