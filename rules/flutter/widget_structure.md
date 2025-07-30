# Flutter 위젯 구조 규칙 (Widget Structure Rules)

## 1. 위젯 클래스 구조

### StatelessWidget 구조
```dart
// Good - 일관된 구조
class UserProfileCard extends StatelessWidget {
  const UserProfileCard({
    super.key,
    required this.user,
    this.onTap,
  });

  final User user;
  final VoidCallback? onTap;

  @override
  Widget build(BuildContext context) {
    return Card(
      child: InkWell(
        onTap: onTap,
        child: Padding(
          padding: const EdgeInsets.all(16),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              _buildHeader(),
              const SizedBox(height: 8),
              _buildContent(),
            ],
          ),
        ),
      ),
    );
  }

  Widget _buildHeader() {
    return Row(
      children: [
        CircleAvatar(
          backgroundImage: NetworkImage(user.avatarUrl),
        ),
        const SizedBox(width: 12),
        Text(
          user.name,
          style: const TextStyle(
            fontSize: 18,
            fontWeight: FontWeight.bold,
          ),
        ),
      ],
    );
  }

  Widget _buildContent() {
    return Text(user.bio);
  }
}
```

### StatefulWidget 구조
```dart
// Good - 생명주기 순서 준수
class AnimatedCounter extends StatefulWidget {
  const AnimatedCounter({
    super.key,
    required this.initialValue,
    this.duration = const Duration(milliseconds: 300),
  });

  final int initialValue;
  final Duration duration;

  @override
  State<AnimatedCounter> createState() => _AnimatedCounterState();
}

class _AnimatedCounterState extends State<AnimatedCounter>
    with SingleTickerProviderStateMixin {
  
  // 1. 멤버 변수
  late AnimationController _controller;
  late Animation<double> _animation;
  late int _currentValue;

  // 2. 생명주기 메서드 (순서대로)
  @override
  void initState() {
    super.initState();
    _currentValue = widget.initialValue;
    _initializeAnimation();
  }

  @override
  void didUpdateWidget(AnimatedCounter oldWidget) {
    super.didUpdateWidget(oldWidget);
    if (oldWidget.duration != widget.duration) {
      _controller.duration = widget.duration;
    }
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return AnimatedBuilder(
      animation: _animation,
      builder: (context, child) {
        return Text(
          _currentValue.toString(),
          style: Theme.of(context).textTheme.headlineMedium,
        );
      },
    );
  }

  // 3. 헬퍼 메서드
  void _initializeAnimation() {
    _controller = AnimationController(
      duration: widget.duration,
      vsync: this,
    );
    _animation = Tween<double>(
      begin: 0,
      end: 1,
    ).animate(CurvedAnimation(
      parent: _controller,
      curve: Curves.easeInOut,
    ));
  }

  // 4. 공개 메서드
  void increment() {
    setState(() {
      _currentValue++;
    });
    _controller.forward(from: 0);
  }
}
```

## 2. 위젯 분리 규칙

### 단일 책임 원칙
```dart
// Good - 각 위젯이 하나의 역할
class ProductListScreen extends StatelessWidget {
  const ProductListScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Products')),
      body: Column(
        children: [
          const ProductSearchBar(),
          const ProductFilterChips(),
          const Expanded(
            child: ProductGrid(),
          ),
        ],
      ),
    );
  }
}

class ProductSearchBar extends StatelessWidget {
  const ProductSearchBar({super.key});

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.all(16),
      child: TextField(
        decoration: const InputDecoration(
          hintText: 'Search products...',
          prefixIcon: Icon(Icons.search),
        ),
        onChanged: (value) {
          // 검색 로직
        },
      ),
    );
  }
}

// Bad - 하나의 위젯에서 모든 것 처리
class ProductListScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Products')),
      body: Column(
        children: [
          // 검색바, 필터, 리스트가 모두 한 곳에 정의
          // 코드가 길어지고 관리가 어려움
        ],
      ),
    );
  }
}
```

### 재사용 가능한 위젯
```dart
// Good - 재사용 가능한 컴포넌트
class CustomButton extends StatelessWidget {
  const CustomButton({
    super.key,
    required this.text,
    required this.onPressed,
    this.variant = ButtonVariant.primary,
    this.size = ButtonSize.medium,
    this.isLoading = false,
  });

  final String text;
  final VoidCallback? onPressed;
  final ButtonVariant variant;
  final ButtonSize size;
  final bool isLoading;

  @override
  Widget build(BuildContext context) {
    return SizedBox(
      height: _getHeight(),
      child: ElevatedButton(
        onPressed: isLoading ? null : onPressed,
        style: _getButtonStyle(context),
        child: isLoading
            ? _buildLoadingIndicator()
            : Text(text),
      ),
    );
  }

  double _getHeight() {
    switch (size) {
      case ButtonSize.small:
        return 32;
      case ButtonSize.medium:
        return 40;
      case ButtonSize.large:
        return 48;
    }
  }

  ButtonStyle _getButtonStyle(BuildContext context) {
    final theme = Theme.of(context);
    switch (variant) {
      case ButtonVariant.primary:
        return ElevatedButton.styleFrom(
          backgroundColor: theme.primaryColor,
          foregroundColor: Colors.white,
        );
      case ButtonVariant.secondary:
        return ElevatedButton.styleFrom(
          backgroundColor: theme.cardColor,
          foregroundColor: theme.textTheme.bodyLarge?.color,
        );
    }
  }

  Widget _buildLoadingIndicator() {
    return SizedBox(
      width: 16,
      height: 16,
      child: CircularProgressIndicator(
        strokeWidth: 2,
        valueColor: AlwaysStoppedAnimation<Color>(
          variant == ButtonVariant.primary ? Colors.white : Colors.grey,
        ),
      ),
    );
  }
}

enum ButtonVariant { primary, secondary }
enum ButtonSize { small, medium, large }
```

## 3. 위젯 트리 최적화

### const 생성자 사용
```dart
// Good - const 생성자로 불필요한 리빌드 방지
class WelcomeMessage extends StatelessWidget {
  const WelcomeMessage({super.key});

  @override
  Widget build(BuildContext context) {
    return const Column(
      children: [
        Icon(
          Icons.wave,
          size: 48,
        ),
        SizedBox(height: 16),
        Text(
          'Welcome!',
          style: TextStyle(
            fontSize: 24,
            fontWeight: FontWeight.bold,
          ),
        ),
      ],
    );
  }
}

// Bad - const 누락으로 매번 새 객체 생성
Widget build(BuildContext context) {
  return Column(
    children: [
      Icon(Icons.wave, size: 48),  // const 누락
      SizedBox(height: 16),        // const 누락
      Text('Welcome!'),            // const 누락
    ],
  );
}
```

### Builder 위젯 활용
```dart
// Good - 필요한 부분만 리빌드
class UserProfile extends StatelessWidget {
  const UserProfile({super.key});

  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        const UserAvatar(),  // 항상 동일
        const SizedBox(height: 16),
        
        // 사용자 정보만 리빌드
        GetBuilder<UserController>(
          id: 'user_info',
          builder: (controller) {
            return Column(
              children: [
                Text(controller.user.name),
                Text(controller.user.email),
              ],
            );
          },
        ),
        
        const UserActions(),  // 항상 동일
      ],
    );
  }
}
```

## 4. 위젯 네이밍

### 명확한 위젯명
```dart
// Good - 목적이 명확한 이름
class ProductSearchTextField extends StatelessWidget {}
class ShoppingCartIcon extends StatelessWidget {}
class UserProfileAvatar extends StatelessWidget {}
class PaymentMethodSelector extends StatelessWidget {}

// Bad - 모호한 이름
class MyWidget extends StatelessWidget {}
class CustomContainer extends StatelessWidget {}
class Helper extends StatelessWidget {}
```

### 스크린과 위젯 구분
```dart
// Good - Screen 접미사로 화면 구분
class HomeScreen extends StatelessWidget {}
class ProfileScreen extends StatelessWidget {}
class SettingsScreen extends StatelessWidget {}

// 일반 위젯은 기능명
class LoadingIndicator extends StatelessWidget {}
class ErrorMessage extends StatelessWidget {}
class ProductCard extends StatelessWidget {}
```

## 5. 위젯 매개변수

### 필수/선택 매개변수 구분
```dart
// Good - 명확한 매개변수 구분
class ProductCard extends StatelessWidget {
  const ProductCard({
    super.key,
    required this.product,      // 필수
    required this.onTap,        // 필수
    this.showPrice = true,      // 선택 (기본값 있음)
    this.elevation,             // 선택 (null 허용)
  });

  final Product product;
  final VoidCallback onTap;
  final bool showPrice;
  final double? elevation;
  
  // 구현...
}
```

### 콜백 함수 네이밍
```dart
// Good - 명확한 콜백 이름
class CustomTextField extends StatelessWidget {
  const CustomTextField({
    super.key,
    this.onChanged,
    this.onSubmitted,
    this.onTap,
    this.onFocusChanged,
  });

  final ValueChanged<String>? onChanged;
  final ValueChanged<String>? onSubmitted;
  final VoidCallback? onTap;
  final ValueChanged<bool>? onFocusChanged;
  
  // 구현...
}
```

## 6. 조건부 렌더링

### 명확한 조건부 렌더링
```dart
// Good - 명확한 조건 처리
Widget build(BuildContext context) {
  return Column(
    children: [
      const Header(),
      
      // 로딩 상태
      if (isLoading)
        const LoadingIndicator()
      else if (hasError)
        ErrorMessage(error: error)
      else if (items.isEmpty)
        const EmptyState()
      else
        ItemList(items: items),
      
      const Footer(),
    ],
  );
}

// Good - 복잡한 조건은 별도 메서드로
Widget build(BuildContext context) {
  return Column(
    children: [
      const Header(),
      _buildContent(),
      const Footer(),
    ],
  );
}

Widget _buildContent() {
  if (isLoading) {
    return const LoadingIndicator();
  }
  
  if (hasError) {
    return ErrorMessage(error: error);
  }
  
  if (items.isEmpty) {
    return const EmptyState();
  }
  
  return ItemList(items: items);
}
```