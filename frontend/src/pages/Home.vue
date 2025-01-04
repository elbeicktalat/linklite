<template>
  <div class="m-5">

	<div class="flex items-baseline justify-between mb-4">
		<h2 class=" text-gray-900 font-semibold">Links</h2>
		<Button variant="solid" @click="createDialogShown = true">Create</Button>
	</div>

	<ListView
	v-if="links.list.data"
	rowKey="name"
	:columns="[{
		label: 'Short Link',
		key: 'name',
		width: 0.4
	},
	{
		label: 'Destination',
		key: 'destination_url'
	},
	{
		label: 'Description',
		key: 'description'
	}]"

	:rows="links.list.data"

	:options="{
		showTooltip: false,
		selectable: false
	}"
	 />


	 <Dialog :options="{
		title: 'New Short Link',
		size: 'xl',
		actions: [
			{
				label: 'Create',
				variant: 'solid',
				onClick(close) {
					links.insert.submit({
						...newLink
					}, {
						onSuccess() {
							newLink.short_link = ''
							newLink.description = ''
							newLink.destination_url = ''
							close();
						}
					})
				}
			}
		]
	 }" v-model="createDialogShown">
		<template #body-content>
			<form class="space-y-3">
				<FormControl
					type="text"
					label="Destination URL"
					placeholder="https://youtube.com/@buildwithhussain"
					v-model="newLink.destination_url"
				/>

				<FormControl
					type="text"
					placeholder="bwh"
					label="Short Link"
					v-model="newLink.short_link"
				/>

				<FormControl
					type="textarea"
					label="Description"
					v-model="newLink.description"
				/>
			</form>

			<ErrorMessage class="mt-2" :message="links.insert.error" />
		</template>
	 </Dialog>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { ListView, Dialog, FormControl, ErrorMessage } from 'frappe-ui'
import { createListResource } from 'frappe-ui'
import { reactive } from 'vue'

const createDialogShown = ref(false)
const newLink = reactive({
	short_link: '',
	destination_url: '',
	description: ''
})

const links = createListResource({
	doctype: 'Short Link',
	fields: ['name', 'destination_url', 'description'],
	 orderBy: 'creation desc'
})

links.fetch()
</script>
