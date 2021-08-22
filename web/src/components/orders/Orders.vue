<template>
	<div>
		<table>
			<thead>
				<tr>
					<th>#</th>
					<th>Username</th>
					<th>E-Mail</th>
					<th>Phone number</th>
					<th>Orders</th>
					<th>View</th>
				</tr>
			</thead>
			<tbody>
				<tr
					v-for="(order, index) in get_orders"
					:key="index"
				>
					<td>{{ index + 1 }}</td>
					<td>{{ order.user.username }}</td>
					<td>{{ order.user.email }}</td>
					<td>{{ order.user.phone_number }}</td>
					<td>{{ order.transactions.length }}</td>
					<td>
						<router-link
							:to="{
								name: 'UserOrders',
								params: {
									username: order.user.username
								}
							}">
							<button class="p-1 px-2">
								<i class="fas fa-eye"></i>
							</button>
						</router-link>
					</td>
				</tr>
			</tbody>
		</table>
	</div>
</template>

<script type="text/javascript">
	export default {
		name: 'Orders',
		props: {
			orders: Array
		},
		computed: {
			get_orders () {
				return this.orders
			}
		}
	}
</script>
