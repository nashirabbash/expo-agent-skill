---
title: "ScrollView"
description: "A scrollable container that supports vertical or horizontal scrolling."
source_url: "https://docs.expo.dev/versions/latest/sdk/ui/universal/scrollview.md"
scraped_at: "2026-07-15T09:01:41.841054"
---

---
title: ScrollView
description: A scrollable container that supports vertical or horizontal scrolling.
sourceCodeUrl: 'https://github.com/expo/expo/tree/sdk-57/packages/expo-ui'
packageName: '@expo/ui'
platforms: ['android', 'ios', 'web', 'expo-go']
---



This documentation is available as Markdown for AI agents and LLMs. See the [full Markdown index](/llms.txt) or append .md to any documentation URL.

# ScrollView

A scrollable container that supports vertical or horizontal scrolling.
Android, iOS, Web, Included in Expo Go

A scrollable container, defaulting to vertical scrolling. Use [`direction="horizontal"`](/versions/latest/sdk/ui/universal/scrollview.md#direction) for horizontal lists.

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

### Vertical scrolling

```tsx
import { Host, ScrollView, Column, Text } from '@expo/ui';

export default function VerticalScrollViewExample() {
  return (
    <Host style={{ flex: 1 }}>
      <ScrollView>
        <Column spacing={8}>
          {Array.from({ length: 30 }).map((_, i) => (
            <Text key={i}>Row {i + 1}</Text>
          ))}
        </Column>
      </ScrollView>
    </Host>
  );
}
```

### Horizontal scrolling

```tsx
import { Host, ScrollView, Row, Text } from '@expo/ui';

export default function HorizontalScrollViewExample() {
  return (
    <Host style={{ flex: 1 }}>
      <ScrollView direction="horizontal">
        <Row spacing={12}>
          {Array.from({ length: 20 }).map((_, i) => (
            <Text key={i}>Item {i + 1}</Text>
          ))}
        </Row>
      </ScrollView>
    </Host>
  );
}
```

## API

```tsx
import { ScrollView } from '@expo/ui';
```

## Component

### `ScrollView`

Supported platforms: Android, iOS, Web.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[ScrollViewProps](#scrollviewprops)\>

A scrollable container that supports vertical or horizontal scrolling.

Props for the [`ScrollView`](#scrollview) component.

ScrollViewProps

### `children`

Supported platforms: Android, iOS, Web.

Optional • Type: [ReactNode](https://reactnative.dev/docs/react-node)

Content to render inside the scroll view.

### `direction`

Supported platforms: Android, iOS, Web.

Optional • Literal type: `string` • Default: `'vertical'`

Scroll direction.

Acceptable values are: `'vertical'` | `'horizontal'`

### `disabled`

Supported platforms: Android, iOS, Web.

Optional • Type: `boolean`

Whether the component is disabled. Disabled components do not respond to user interaction.

### `hidden`

Supported platforms: Android, iOS, Web.

Optional • Type: `boolean`

Whether the component is hidden.

### `modifiers`

Supported platforms: Android, iOS.

Optional • Type: `ModifierConfig[]`

Platform-specific modifier escape hatch. Pass an array of modifier configs from `@expo/ui/swift-ui/modifiers` or `@expo/ui/jetpack-compose/modifiers`. A modifier supplied here replaces any modifier of the same type that the component derives from `style` or other props.

### `onAppear`

Supported platforms: Android, iOS, Web.

Optional • Type: `() => void`

Called when the component appears on screen.

### `onDisappear`

Supported platforms: Android, iOS, Web.

Optional • Type: `() => void`

Called when the component is removed from screen.

### `onPress`

Supported platforms: Android, iOS, Web.

Optional • Type: `() => void`

Called when the component is pressed.

### `showsIndicators`

Supported platforms: iOS, Web.

Optional • Type: `boolean` • Default: `true`

Whether to show scroll indicators.

### `style`

Supported platforms: Android, iOS, Web.

Optional • Type: [Pick](https://www.typescriptlang.org/docs/handbook/utility-types.html#picktype-keys)<[ViewStyle](https://reactnative.dev/docs/view-style-props), 'padding' | 'paddingHorizontal' | 'paddingVertical' | 'paddingTop' | 'paddingBottom' | 'paddingLeft' | 'paddingRight' | 'backgroundColor' | 'borderRadius' | 'borderWidth' | 'borderColor' | 'opacity' | 'width' | 'height'\>

Platform-agnostic style properties. These are translated to SwiftUI modifiers on iOS and Jetpack Compose modifiers on Android.

### `testID`

Supported platforms: Android, iOS, Web.

Optional • Type: `string`

Identifier used to locate the component in end-to-end tests.
