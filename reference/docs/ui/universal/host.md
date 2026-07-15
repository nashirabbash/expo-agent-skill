---
title: "Host"
description: "A cross-platform Host component that wraps universal @expo/ui content."
source_url: "https://docs.expo.dev/versions/latest/sdk/ui/universal/host.md"
scraped_at: "2026-07-15T09:01:36.087492"
---

---
title: Host
description: A cross-platform Host component that wraps universal @expo/ui content.
sourceCodeUrl: 'https://github.com/expo/expo/tree/sdk-57/packages/expo-ui'
packageName: '@expo/ui'
platforms: ['android', 'ios', 'web', 'expo-go']
---



This documentation is available as Markdown for AI agents and LLMs. See the [full Markdown index](/llms.txt) or append .md to any documentation URL.

# Host

A cross-platform Host component that wraps universal @expo/ui content.
Android, iOS, Web, Included in Expo Go

A container for universal `@expo/ui` content. On Android and iOS it re-exports the platform-native [`Host` for Jetpack Compose](/versions/latest/sdk/ui/jetpack-compose/host.md)/[`Host` for SwiftUI](/versions/latest/sdk/ui/swift-ui/host.md), so Jetpack Compose/SwiftUI children render exactly as they would in the platform-specific packages. On web, it falls back to a React Native [`View`](https://reactnative.dev/docs/view). Use `Host` as the root of any universal subtree so the same component tree works across all three platforms.

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

### Basic usage

```tsx
import { Host, Column, Text, Button } from '@expo/ui';

export default function HostExample() {
  return (
    <Host style={{ flex: 1 }}>
      <Column spacing={12} alignment="center">
        <Text>Hello, world!</Text>
        <Button label="Press me" onPress={() => alert('Pressed')} />
      </Column>
    </Host>
  );
}
```

### Match contents sizing

Use `matchContents` to let `Host` size itself to fit its content. On Android and iOS, this is forwarded to the platform-native `Host` (see [Jetpack Compose](/versions/latest/sdk/ui/jetpack-compose/host.md)/[SwiftUI](/versions/latest/sdk/ui/swift-ui/host.md) for the exact platform semantics). On web, it applies `alignSelf: 'flex-start'` to the underlying `View` so the host shrinks to fit its children instead of being stretched by its parent.

> **Note:** On web, the per-axis form (`{ horizontal: true }` / `{ vertical: true }`) behaves the same as the boolean form, since `alignSelf` only controls stretching on the parent's cross axis. Components that rely on independent per-axis sizing should expect the same shrink-to-fit behavior on web regardless of which axis is opted in.

```tsx
import { Host, Button } from '@expo/ui';

export default function MatchContentsExample() {
  return (
    <Host matchContents>
      <Button label="Sized to content" onPress={() => {}} />
    </Host>
  );
}
```

### Layout direction

Use `layoutDirection` to render the subtree as left-to-right or right-to-left. On Android and iOS, this is forwarded to the platform-native `Host` (see [Jetpack Compose](/versions/latest/sdk/ui/jetpack-compose/host.md)/[SwiftUI](/versions/latest/sdk/ui/swift-ui/host.md) for the exact platform semantics). On web, it sets the `dir` attribute on the underlying `View` so descendants inherit the chosen direction.

```tsx
import { Host, Row, Text } from '@expo/ui';

export default function LayoutDirectionExample() {
  return (
    <Host layoutDirection="rightToLeft">
      <Row spacing={8}>
        <Text>First</Text>
        <Text>Second</Text>
      </Row>
    </Host>
  );
}
```

### Reacting to content layout

Use `onLayoutContent` to be notified of the current dimensions of the host's content. On Android and iOS, this is forwarded to the platform-native `Host` (see [Jetpack Compose](/versions/latest/sdk/ui/jetpack-compose/host.md)/[SwiftUI](/versions/latest/sdk/ui/swift-ui/host.md) for the exact platform semantics). On web, it is derived from the underlying `View`'s `onLayout` callback.

```tsx
import { Host, Text } from '@expo/ui';

export default function OnLayoutContentExample() {
  return (
    <Host
      matchContents
      onLayoutContent={({ nativeEvent: { width, height } }) =>
        console.log(`content size: ${width}x${height}`)
      }>
      <Text>Hello, world!</Text>
    </Host>
  );
}
```

### Filling the viewport

Use `useViewportSizeMeasurement` for content that should size to the available viewport space. On Android and iOS, this is forwarded to the platform-native `Host` (see [Jetpack Compose](/versions/latest/sdk/ui/jetpack-compose/host.md)/[SwiftUI](/versions/latest/sdk/ui/swift-ui/host.md) for the exact platform semantics). On web, the host's underlying `View` is given the current window's width and height; any explicit `style` you pass still wins.

```tsx
import { Host, Column, Text } from '@expo/ui';

export default function UseViewportSizeMeasurementExample() {
  return (
    <Host useViewportSizeMeasurement>
      <Column spacing={12} alignment="center">
        <Text>Fills the viewport</Text>
      </Column>
    </Host>
  );
}
```

### Ignoring safe areas

By default, `Host` respects the device safe area insets (notch, home indicator, and so on). Use `ignoreSafeArea="all"` to let content extend edge-to-edge, or `ignoreSafeArea="keyboard"` to keep safe-area padding but ignore the keyboard inset. On Android and iOS, this is forwarded to the platform-native `Host` (see [Jetpack Compose](/versions/latest/sdk/ui/jetpack-compose/host.md)/[SwiftUI](/versions/latest/sdk/ui/swift-ui/host.md) for the exact platform semantics). On web, it is implemented via the CSS `env(safe-area-inset-*)` values applied as padding on the underlying `View`; the default also folds in `env(keyboard-inset-*)` for pages that opt in to the [VirtualKeyboard API](https://developer.mozilla.org/en-US/docs/Web/API/VirtualKeyboard_API).

```tsx
import { Host, Text } from '@expo/ui';

export default function IgnoreSafeAreaExample() {
  return (
    <Host ignoreSafeArea="all">
      <Text>Extends behind the notch and home indicator</Text>
    </Host>
  );
}
```

### Forcing a color scheme

Use `colorScheme` to override the appearance of descendant native views. Pass `'light'` or `'dark'` to force one, or omit it to follow the device setting. Android and iOS only — ignored on web.

```tsx
import { Host, Button } from '@expo/ui';

export default function HostColorSchemeExample() {
  return (
    <Host colorScheme="dark" style={{ flex: 1 }}>
      <Button label="Always dark" onPress={() => {}} />
    </Host>
  );
}
```

## API

```tsx
import { Host } from '@expo/ui';
```

## Component

### `Host`

Supported platforms: Android, iOS, Web.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[UniversalHostProps](#universalhostprops)\>

A bridging container that hosts SwiftUI views on iOS and Jetpack Compose views on Android. On platforms without a native UI-toolkit binding (web, RN fallback), renders a plain `View`.

## Props

### `children`

Supported platforms: Android, iOS, Web.

Optional • Type: [ReactNode](https://reactnative.dev/docs/react-node)

### `colorScheme`

Supported platforms: Android, iOS, Web.

Optional • Type: `ColorSchemeName`

The color scheme to apply to the subtree. `'light'` / `'dark'` force a specific appearance; omitted follows the device setting.

### `ignoreSafeArea`

Supported platforms: Android, iOS, Web.

Optional • Literal type: `string`

Controls which safe area regions the hosting view should ignore. Can only be set once on mount.

-   `'all'`- ignores all safe area insets.
-   `'keyboard'` - ignores only the keyboard safe area.

Acceptable values are: `'all'` | `'keyboard'`

### `layoutDirection`

Supported platforms: Android, iOS, Web.

Optional • Literal type: `string`

Layout direction for the platform UI content. Defaults to the current locale direction from `I18nManager`.

Acceptable values are: `'leftToRight'` | `'rightToLeft'`

### `matchContents`

Supported platforms: Android, iOS, Web.

Optional • Literal type: `union` • Default: `false`

When `true`, the host updates its size in the React Native view tree to match the content's layout from the underlying platform UI toolkit. Can only be set once on mount.

Acceptable values are: `boolean` | `{ horizontal: boolean, vertical: boolean }`

### `onLayoutContent`

Supported platforms: Android, iOS, Web.

Optional • Type: `(event: { nativeEvent: { height: number, width: number } }) => void`

Callback function that is triggered when the content completes its layout. Provides the current dimensions of the content, which may change as the content updates.

### `seedColor`

Supported platforms: Android, iOS, Web.

Optional • Type: [ColorValue](https://reactnative.dev/docs/colors)

Seed color used to derive the theme applied to the host's subtree. Each platform interprets it natively:

-   On Android, it generates a full Material 3 palette (`SchemeTonalSpot`, the same algorithm as Material You) that themes Compose children and is exposed to descendants via `useMaterialColors()`.
-   On iOS, it is applied as the SwiftUI tint, propagating through the environment to theme interactive controls such as buttons, switches, and sliders.
-   On web, it generates a primary color scale exposed as CSS variables to the subtree.

When omitted, each platform falls back to its default theme.

### `useViewportSizeMeasurement`

Supported platforms: Android, iOS, Web.

Optional • Type: `boolean` • Default: `false`

When true and no explicit size is provided, the host will use the viewport size as the proposed size for layout. This is particularly useful for views that need to fill their available space, such as `List`.

### Inherited Props

-   [ViewProps](https://reactnative.dev/docs/view#props)
