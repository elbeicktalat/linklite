<template>
	<div>
		<h2 class="font-bold text-gray-800">Analytics</h2>
	</div>
	<div class="grid grid-cols-5 justify-start items-start">
		<NumberChart
			:config="{
				title: 'Total Clicks',
				value: analyticsData.totalClicks,
			}"
  		/>

		<div class="col-span-2">
		<AxisChart
			:config="{
				data: analyticsData.clicksByLink,
				title: 'Clicks by Link',
				subtitle: 'Number of clicks per link',
				xAxis: {
					key: 'link',
					title: 'Link',
					type: 'category',
				},
				yAxis: {
					title: 'Clicks',
				},
				swapXY: true,
				series: [
					{
						name: 'clicks',
						type: 'bar',
					},
				],
			}"
			/>
		</div>
	</div>
</template>

<script setup>
import { NumberChart, AxisChart, createResource, createListResource } from 'frappe-ui';
import { reactive } from 'vue';

const analyticsData = reactive({
	totalClicks: 0,
	clicksByLink: []
})

createResource({
	url: 'frappe.client.get_count',
	params: {
		doctype: 'Short Link Click'
	},
	onSuccess(count) {
		analyticsData.totalClicks = count;
	},
	auto: true
})

createListResource({
	doctype: 'Short Link Click',
	fields: ['link', 'count(name) as clicks'],
	groupBy: 'link',
	onSuccess(data) {
		analyticsData.clicksByLink = data;
	},
	auto: true
})
</script>
