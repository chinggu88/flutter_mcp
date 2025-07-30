# Flutter 상태 관리 규칙 (State Management Rules)

## 1. 상태 관리 계층

### 로컬 상태 vs 전역 상태
```dart
// Good - 로컬 상태 (StatefulWidget)
class CounterWidget extends StatefulWidget {
  const CounterWidget({super.key});

  @override
  State<CounterWidget> createState() => _CounterWidgetState();
}

class _CounterWidgetState extends State<CounterWidget> {
  int _count = 0;  // 이 위젯에서만 사용되는 상태

  void _increment() {
    setState(() {
      _count++;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        Text('Count: $_count'),
        ElevatedButton(
          onPressed: _increment,
          child: const Text('Increment'),
        ),
      ],
    );
  }
}

// Good - 전역 상태 (GetX Controller)
class AuthController extends GetxController {
  final Rx<User?> _user = Rx<User?>(null);  // 앱 전체에서 사용
  
  User? get user => _user.value;
  bool get isAuthenticated => _user.value != null;

  Future<void> login(String email, String password) async {
    try {
      final user = await authService.login(email, password);
      _user.value = user;
    } catch (e) {
      // 에러 처리
    }
  }

  void logout() {
    _user.value = null;
  }
}
```

## 2. 상태 불변성

### 상태 변경 시 불변성 유지
```dart
// Good - 불변성 유지
class TodoController extends GetxController {
  final RxList<Todo> _todos = <Todo>[].obs;
  
  List<Todo> get todos => _todos.toList();  // 복사본 반환

  void addTodo(String title) {
    final newTodo = Todo(
      id: DateTime.now().millisecondsSinceEpoch.toString(),
      title: title,
      isCompleted: false,
    );
    _todos.add(newTodo);
  }

  void toggleTodo(String id) {
    final index = _todos.indexWhere((todo) => todo.id == id);
    if (index != -1) {
      // 새 객체 생성으로 불변성 유지
      _todos[index] = _todos[index].copyWith(
        isCompleted: !_todos[index].isCompleted,
      );
    }
  }

  void updateTodo(String id, String newTitle) {
    final index = _todos.indexWhere((todo) => todo.id == id);
    if (index != -1) {
      _todos[index] = _todos[index].copyWith(title: newTitle);
    }
  }
}

// Todo 모델에 copyWith 메서드 필요
class Todo {
  final String id;
  final String title;
  final bool isCompleted;

  const Todo({
    required this.id,
    required this.title,
    required this.isCompleted,
  });

  Todo copyWith({
    String? id,
    String? title,
    bool? isCompleted,
  }) {
    return Todo(
      id: id ?? this.id,
      title: title ?? this.title,
      isCompleted: isCompleted ?? this.isCompleted,
    );
  }
}
```

## 3. 상태 구조화

### 명확한 상태 분류
```dart
// Good - 상태를 논리적으로 그룹화
class ProductController extends GetxController {
  // UI 상태
  final RxBool _isLoading = false.obs;
  final RxBool _isRefreshing = false.obs;
  final Rx<String?> _error = Rx<String?>(null);

  // 데이터 상태
  final RxList<Product> _products = <Product>[].obs;
  final RxList<Category> _categories = <Category>[].obs;
  
  // 필터/검색 상태
  final RxString _searchQuery = ''.obs;
  final Rx<Category?> _selectedCategory = Rx<Category?>(null);
  final RxList<Product> _filteredProducts = <Product>[].obs;

  // Getters
  bool get isLoading => _isLoading.value;
  bool get isRefreshing => _isRefreshing.value;
  String? get error => _error.value;
  List<Product> get products => _products.toList();
  List<Product> get filteredProducts => _filteredProducts.toList();
  String get searchQuery => _searchQuery.value;
  Category? get selectedCategory => _selectedCategory.value;

  // Actions
  Future<void> fetchProducts() async {
    _setLoading(true);
    _clearError();
    
    try {
      final products = await productRepository.getProducts();
      _products.assignAll(products);
      _applyFilters();
    } catch (e) {
      _setError('Failed to fetch products: ${e.toString()}');
    } finally {
      _setLoading(false);
    }
  }

  void searchProducts(String query) {
    _searchQuery.value = query;
    _applyFilters();
  }

  void selectCategory(Category? category) {
    _selectedCategory.value = category;
    _applyFilters();
  }

  // Private methods
  void _setLoading(bool loading) {
    _isLoading.value = loading;
  }

  void _setError(String? error) {
    _error.value = error;
  }

  void _clearError() {
    _error.value = null;
  }

  void _applyFilters() {
    var filtered = _products.toList();

    // 검색 필터
    if (_searchQuery.value.isNotEmpty) {
      filtered = filtered.where((product) =>
        product.name.toLowerCase().contains(_searchQuery.value.toLowerCase())
      ).toList();
    }

    // 카테고리 필터
    if (_selectedCategory.value != null) {
      filtered = filtered.where((product) =>
        product.categoryId == _selectedCategory.value!.id
      ).toList();
    }

    _filteredProducts.assignAll(filtered);
  }
}
```

## 4. 상태 업데이트 패턴

### 비동기 상태 처리
```dart
// Good - 명확한 비동기 상태 관리
class UserController extends GetxController {
  final Rx<AsyncState<User>> _userState = AsyncState<User>.initial().obs;
  
  AsyncState<User> get userState => _userState.value;
  User? get user => _userState.value.data;
  bool get isLoading => _userState.value.isLoading;
  String? get error => _userState.value.error;

  Future<void> loadUser(String userId) async {
    _userState.value = AsyncState<User>.loading();
    
    try {
      final user = await userRepository.getUser(userId);
      _userState.value = AsyncState<User>.success(user);
    } catch (e) {
      _userState.value = AsyncState<User>.error(e.toString());
    }
  }

  Future<void> updateUser(User updatedUser) async {
    // 낙관적 업데이트
    final previousState = _userState.value;
    _userState.value = AsyncState<User>.success(updatedUser);
    
    try {
      await userRepository.updateUser(updatedUser);
    } catch (e) {
      // 실패 시 이전 상태로 롤백
      _userState.value = previousState;
      Get.snackbar('Error', 'Failed to update user');
    }
  }
}

// AsyncState 유틸리티 클래스
class AsyncState<T> {
  final T? data;
  final String? error;
  final bool isLoading;

  const AsyncState._({
    this.data,
    this.error,
    this.isLoading = false,
  });

  factory AsyncState.initial() => const AsyncState._();
  
  factory AsyncState.loading([T? data]) => AsyncState._(
    data: data,
    isLoading: true,
  );
  
  factory AsyncState.success(T data) => AsyncState._(data: data);
  
  factory AsyncState.error(String error, [T? data]) => AsyncState._(
    data: data,
    error: error,
  );

  bool get hasError => error != null;
  bool get hasData => data != null;
}
```

## 5. 상태 감시 및 반응

### Reactive Programming 패턴
```dart
// Good - 상태 변화에 반응하는 패턴
class ShoppingCartController extends GetxController {
  final RxList<CartItem> _items = <CartItem>[].obs;
  final RxDouble _totalPrice = 0.0.obs;
  final RxInt _itemCount = 0.obs;

  List<CartItem> get items => _items.toList();
  double get totalPrice => _totalPrice.value;
  int get itemCount => _itemCount.value;

  @override
  void onInit() {
    super.onInit();
    
    // 아이템 변화 감시하여 자동으로 총합 계산
    ever(_items, (_) => _calculateTotals());
  }

  void addItem(Product product) {
    final existingIndex = _items.indexWhere(
      (item) => item.product.id == product.id
    );

    if (existingIndex >= 0) {
      _items[existingIndex] = _items[existingIndex].copyWith(
        quantity: _items[existingIndex].quantity + 1,
      );
    } else {
      _items.add(CartItem(product: product, quantity: 1));
    }
  }

  void removeItem(String productId) {
    _items.removeWhere((item) => item.product.id == productId);
  }

  void updateQuantity(String productId, int quantity) {
    if (quantity <= 0) {
      removeItem(productId);
      return;
    }

    final index = _items.indexWhere(
      (item) => item.product.id == productId
    );
    
    if (index >= 0) {
      _items[index] = _items[index].copyWith(quantity: quantity);
    }
  }

  void clear() {
    _items.clear();
  }

  void _calculateTotals() {
    double total = 0.0;
    int count = 0;
    
    for (final item in _items) {
      total += item.product.price * item.quantity;
      count += item.quantity;
    }
    
    _totalPrice.value = total;
    _itemCount.value = count;
  }
}
```

## 6. 상태 지속성

### 상태 저장 및 복원
```dart
// Good - 상태 지속성 관리
class SettingsController extends GetxController {
  final RxBool _isDarkMode = false.obs;
  final RxString _language = 'ko'.obs;
  final RxBool _notificationsEnabled = true.obs;

  bool get isDarkMode => _isDarkMode.value;
  String get language => _language.value;
  bool get notificationsEnabled => _notificationsEnabled.value;

  @override
  void onInit() {
    super.onInit();
    _loadSettings();
    
    // 상태 변화 감시하여 자동 저장
    ever(_isDarkMode, (_) => _saveSettings());
    ever(_language, (_) => _saveSettings());
    ever(_notificationsEnabled, (_) => _saveSettings());
  }

  void toggleDarkMode() {
    _isDarkMode.value = !_isDarkMode.value;
  }

  void setLanguage(String lang) {
    _language.value = lang;
  }

  void toggleNotifications() {
    _notificationsEnabled.value = !_notificationsEnabled.value;
  }

  Future<void> _loadSettings() async {
    try {
      final prefs = await SharedPreferences.getInstance();
      _isDarkMode.value = prefs.getBool('isDarkMode') ?? false;
      _language.value = prefs.getString('language') ?? 'ko';
      _notificationsEnabled.value = prefs.getBool('notificationsEnabled') ?? true;
    } catch (e) {
      print('Failed to load settings: $e');
    }
  }

  Future<void> _saveSettings() async {
    try {
      final prefs = await SharedPreferences.getInstance();
      await prefs.setBool('isDarkMode', _isDarkMode.value);
      await prefs.setString('language', _language.value);
      await prefs.setBool('notificationsEnabled', _notificationsEnabled.value);
    } catch (e) {
      print('Failed to save settings: $e');
    }
  }
}
```

## 7. 상태 테스트

### 상태 관리 테스트 패턴
```dart
// Good - 상태 변화 테스트
void main() {
  group('TodoController Tests', () {
    late TodoController controller;

    setUp(() {
      controller = TodoController();
    });

    tearDown(() {
      controller.dispose();
    });

    test('should add todo', () {
      // Given
      const title = 'Test Todo';
      expect(controller.todos.length, 0);

      // When
      controller.addTodo(title);

      // Then
      expect(controller.todos.length, 1);
      expect(controller.todos.first.title, title);
      expect(controller.todos.first.isCompleted, false);
    });

    test('should toggle todo completion', () {
      // Given
      controller.addTodo('Test Todo');
      final todoId = controller.todos.first.id;
      expect(controller.todos.first.isCompleted, false);

      // When
      controller.toggleTodo(todoId);

      // Then
      expect(controller.todos.first.isCompleted, true);
    });
  });
}
```