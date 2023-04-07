# 201800538 헝가리어과 김건우 *정상 동작*

# Node 클래스 정의
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
	
# LinkedList 클래스 정의
class LinkedList:

	# 초기화 메소드
	def __init__(self):
		dummy = Node("dummy")
		self.head = dummy
		self.tail = dummy

		self.current = None
		self.before = None

		self.num_of_data = 0
	
	def __str__(self):
		return f"{self.data}"

	# append 메소드 (insert - 맨 뒤에 노드 추가, tail과 node의 next, 데이터 개수 변경)
	def append(self, data):
		new_node = Node(data)
		self.tail.next = new_node
		self.tail = new_node

		self.num_of_data += 1

	# delete 메소드 (delete - current 노드 삭제, 인접 노드의 current, next 변경, 데이터 개수 변경)
	def delete(self):
		pop_data = self.current.data

		if self.current is self.tail:
			self.tail = self.before

		# 중요 : current가 next가 아닌 before로 변경된다.
		self.before.next = self.current.next
		self.current = self.before 

		self.num_of_data -= 1
		return pop_data

	# first 메소드 (search1 - 맨 앞의 노드 검색, before, current 변경)
	def first(self):
		# 데이터가 없는 경우 첫번째 노드도 없기 때문에 None 리턴
		if self.num_of_data == 0: 
			return None

		self.before = self.head
		self.current = self.head.next

		return self.current.data

	# next 메소드 (search2 - current 노드의 다음 노드 검색, 이전에 first 메소드가 한번은 실행되어야 함)
	def next(self):
		if self.current.next == None:
			return None

		self.before = self.current
		self.current = self.current.next

		return self.current.data
	
	# size 메소드
	def size(self):
		return self.num_of_data 

	def traverse_all(self):
		print("\nhead -> ",self.first(), end="")
		for i in range(self.num_of_data):
			print(" -> ",self.next(), end="")

	def insert_at(self, position, new_data):
		if position <= 0:
			print("\nError")
			return
		elif position > self.size():
			self.append(new_data)
		else:
			new_data = Node(new_data)
			self.first()
			for i in range(position-1):
				self.next()
			new_data.next = self.current.next
			self.before.next = new_data
			self.current = self.before.next

	def remove(self, key):
		self.first()
		count = 1
		for i in range(self.size()):
			if self.current.data == key:
				self.delete()
				print(f"{count}번째 원소 {key}를 삭제합니다")
				return
			elif count == self.size():
				print("해당하는 원소가 없습니다.")
				return
			else:
				self.next()
				count += 1
		
test_list = LinkedList()
#test append()
test_list.append(200)
test_list.append(4000)
test_list.append(370)
test_list.append(770)
test_list.append(480)
test_list.append(150)
test_list.append(370)
#test traverse_all()
test_list.traverse_all()
test_list.insert_at(4, 990)
test_list.traverse_all()
#test error msg when position <= 0
test_list.insert_at(0, 990)
test_list.remove(4000)
#test "해당하는 원소가 없습니다" msg
test_list.remove(0)




			
