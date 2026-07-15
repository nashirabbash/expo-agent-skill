---
title: "Host"
description: "A SwiftUI Host component that enables SwiftUI components in React Native."
source_url: "https://docs.expo.dev/versions/latest/sdk/ui/swift-ui/host.md"
scraped_at: "2026-07-15T08:59:17.738819"
---

---
title: Host
description: A SwiftUI Host component that enables SwiftUI components in React Native.
sourceCodeUrl: 'https://github.com/expo/expo/tree/sdk-57/packages/expo-ui'
packageName: '@expo/ui'
platforms: ['ios', 'tvos', 'expo-go']
---



This documentation is available as Markdown for AI agents and LLMs. See the [full Markdown index](/llms.txt) or append .md to any documentation URL.

# Host

A SwiftUI Host component that enables SwiftUI components in React Native.
iOS, tvOS, Included in Expo Go

> For cross-platform usage, see the universal [`Host`](/versions/latest/sdk/ui/universal/host.md) — it renders the appropriate native component per platform.

A component that allows you to put the other `@expo/ui/swift-ui` components in React Native. It acts like [`<svg>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/svg) for DOM, [`<Canvas>`](https://shopify.github.io/react-native-skia/docs/canvas/overview/) for [`react-native-skia`](https://shopify.github.io/react-native-skia/), which underlying uses [`UIHostingController`](https://developer.apple.com/documentation/swiftui/uihostingcontroller) to render the SwiftUI views in UIKit.

Since the `Host` component is a React Native [`View`](https://reactnative.dev/docs/view), you can pass the [`style`](https://reactnative.dev/docs/style) prop to it or `matchContents` prop to make the `Host` component match the contents' size.

## Installation

```sh
# npm
npx expo install @expo/ui

# yarn
yarn expo install @expo/ui

# pnpm
pnpm expo install @expo/ui

# bun
bun expo install @expo/ui
```

If you are installing this in an [existing React Native app](/bare/overview.md), make sure to [install `expo`](/bare/installing-expo-modules.md) in your project.

## Usage

### Match contents sizing

Use `matchContents` to let the `Host` automatically size itself to fit its SwiftUI content, instead of requiring explicit dimensions.

> **Note:** `matchContents` only works correctly with components that have an intrinsic size or an explicit [`frame`](/versions/latest/sdk/ui/swift-ui/modifiers.md#frameparams) (for example, `Button`, `Toggle`, `Text`). Flexible-width components like `Slider` and linear `ProgressView` expand to fill available space and have no intrinsic width, using `matchContents` with them will result in near-zero width. For those components, either apply a [`frame`](/versions/latest/sdk/ui/swift-ui/modifiers.md#frameparams) modifier on the component to give it an explicit width, or use explicit sizing with `style` on the `Host` instead (for example, `style={{ flex: 1 }}` or `style={{ width: 300 }}`).

```tsx
import { Button, Host } from '@expo/ui/swift-ui';

export default function MatchContentsExample() {
  return (
    <Host matchContents>
      <Button
        onPress={() => {
          console.log('Pressed');
        }}>
        Click
      </Button>
    </Host>
  );
}
```

> **Note:** Do not use `matchContents` on the same axis as a scroll container (`ScrollView`, `List`, `Form`, `LazyHStack`, `LazyVStack`). `matchContents` resolves to SwiftUI's `.fixedSize`, which sizes the scroll container to its content. It also leaves nothing past the viewport to scroll into, so scrolling silently stops working. Use `matchContents={{ vertical: true }}` together with `style={{ width: '100%' }}` (or any finite width on the scroll axis).

```tsx
import { Host, HStack, ScrollView, Text } from '@expo/ui/swift-ui';

export default function ScrollViewMatchContents() {
  return (
    <Host matchContents={{ vertical: true }} style={{ width: '100%' }}>
      <ScrollView axes="horizontal">
        <HStack spacing={12}>
          {Array.from({ length: 20 }).map((_, i) => (
            <Text key={i}>Item {i}</Text>
          ))}
        </HStack>
      </ScrollView>
    </Host>
  );
}
```

### Explicit sizing with style

Use `style` to set explicit sizes on the `Host`, such as filling the available space with `flex: 1`.

```tsx
import { Button, Host, VStack, Text } from '@expo/ui/swift-ui';

export default function ExplicitSizingExample() {
  return (
    <Host style={{ flex: 1 }}>
      <VStack spacing={8}>
        <Text>Hello, world!</Text>
        <Button
          onPress={() => {
            console.log('Pressed');
          }}>
          Click
        </Button>
      </VStack>
    </Host>
  );
}
```

### Ignoring keyboard safe area

Use `ignoreSafeArea="keyboard"` when React Native is already handling keyboard avoidance (for example, with `react-native-keyboard-controller`), to prevent the SwiftUI host from applying its own keyboard inset.

```tsx
import { Host, TextField } from '@expo/ui/swift-ui';
import { KeyboardProvider, KeyboardStickyView } from 'react-native-keyboard-controller';
import { View } from 'react-native';

export default function IgnoreKeyboardExample() {
  return (
    <KeyboardProvider>
      <View style={{ flex: 1, backgroundColor: 'black' }}>
        <KeyboardStickyView
          style={{
            position: 'absolute',
            bottom: 0,
            left: 0,
            right: 0,
            padding: 16,
            backgroundColor: 'green',
          }}>
          <Host matchContents ignoreSafeArea="keyboard" style={{ backgroundColor: 'red' }}>
            <TextField placeholder="Enter text" axis="vertical" />
          </Host>
        </KeyboardStickyView>
      </View>
    </KeyboardProvider>
  );
}
```

### Ignoring all safe areas

Use `ignoreSafeArea="all"` when you want SwiftUI content to extend behind the status bar, useful for full-screen overlays or backgrounds.

```tsx
import { Host, Text, VStack } from '@expo/ui/swift-ui';

export default function IgnoreAllSafeAreasExample() {
  return (
    <Host
      ignoreSafeArea="all"
      style={{ position: 'absolute', top: 0, left: 0, right: 0, bottom: 0 }}>
      <VStack>
        <Text>This content extends behind the status bar and home indicator.</Text>
      </VStack>
    </Host>
  );
}
```

## API

```tsx
import { Host } from '@expo/ui/swift-ui';
```

## Component

### `Host`

Supported platforms: iOS, tvOS.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[HostProps](#hostprops)\>

A hosting component for SwiftUI views.

HostProps

### `children`

Supported platforms: iOS, tvOS.

Type: [ReactNode](https://reactnative.dev/docs/react-node)

### `colorScheme`

Supported platforms: iOS, tvOS.

Optional • Literal type: `string`

The color scheme of the host view.

Acceptable values are: `'light'` | `'dark'`

### `ignoreSafeArea`

Supported platforms: iOS, tvOS.

Optional • Literal type: `string`

Controls which safe area regions the SwiftUI hosting view should ignore. Can only be set once on mount.

-   `'all'`- ignores all safe area insets.
-   `'keyboard'` - ignores only the keyboard safe area.

Acceptable values are: `'all'` | `'keyboard'`

### `layoutDirection`

Supported platforms: iOS, tvOS.

Optional • Literal type: `string`

The layout direction for the SwiftUI content. Defaults to the current locale direction from I18nManager.

Acceptable values are: `'leftToRight'` | `'rightToLeft'`

### `matchContents`

Supported platforms: iOS, tvOS.

Optional • Literal type: `union` • Default: `false`

When true, the host view will update its size in the React Native view tree to match the content's layout from SwiftUI. Can be only set once on mount.

Acceptable values are: `boolean` | `{ horizontal: boolean, vertical: boolean }`

### `onLayoutContent`

Supported platforms: iOS, tvOS.

Optional • Type: `(event: { nativeEvent: { height: number, width: number } }) => void`

Callback function that is triggered when the SwiftUI content completes its layout. Provides the current dimensions of the content, which may change as the content updates.

### `pointerEvents`

Supported platforms: iOS, tvOS.

Optional • Literal type: `string`

Acceptable values are: `'box-none'` | `'none'` | `'box-only'` | `'auto'`

### `seedColor`

Supported platforms: iOS, tvOS.

Optional • Type: [ColorValue](https://reactnative.dev/docs/colors)

Seed color applied to the SwiftUI content as its tint. It propagates through the SwiftUI environment to theme interactive elements (buttons, switches, sliders, and similar controls) rendered by the children.

### `style`

Supported platforms: iOS, tvOS.

Optional • Type: StyleProp<[ViewStyle](https://reactnative.dev/docs/view-style-props)\>

### `useViewportSizeMeasurement`

Supported platforms: iOS, tvOS.

Optional • Type: `boolean` • Default: `false`

When true and no explicit size is provided, the host will use the viewport size as the proposed size for SwiftUI layout. This is particularly useful for SwiftUI views that need to fill their available space, such as `Form`.

#### Inherited Props

-   [CommonViewModifierProps](/versions/latest/sdk/ui/swift-ui/modifiers.md)
