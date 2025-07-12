<template>
	<div class="flex h-screen w-full flex-row bg-surface-white shadow">
		<Sidebar :header="{title: 'LinkLite', menuItems: [ { label: 'Toggle Theme', icon: Moon, onClick: toggleTheme },] }" />
		<div class="w-full">
			<slot></slot>
		</div>
	</div>
</template>

<script setup>
import Moon from '~icons/lucide/moon';
import { Sidebar } from 'frappe-ui';

function toggleTheme() {
  const currentTheme = document.documentElement.getAttribute('data-theme');
  const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
  document.documentElement.setAttribute('data-theme', newTheme);
}
</script>
