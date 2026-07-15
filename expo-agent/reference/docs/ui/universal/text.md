---
title: "Text"
description: "A component for displaying styled text content."
source_url: "https://docs.expo.dev/versions/latest/sdk/ui/universal/text.md"
scraped_at: "2026-07-15T09:01:46.091469"
---

---
title: Text
description: A component for displaying styled text content.
sourceCodeUrl: 'https://github.com/expo/expo/tree/sdk-57/packages/expo-ui'
packageName: '@expo/ui'
platforms: ['android', 'ios', 'web', 'expo-go']
---



This documentation is available as Markdown for AI agents and LLMs. See the [full Markdown index](/llms.txt) or append .md to any documentation URL.

# Text

A component for displaying styled text content.
Android, iOS, Web, Included in Expo Go

A component for displaying text. Adapts to the platform color scheme (light/dark) by default and exposes a focused subset of typography knobs through [`textStyle`](/versions/latest/sdk/ui/universal/text.md#textstyle).

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

### Basic text

```tsx
import { Host, Text } from '@expo/ui';

export default function TextExample() {
  return (
    <Host matchContents>
      <Text>Hello, world!</Text>
    </Host>
  );
}
```

### Styled text

Use [`textStyle`](/versions/latest/sdk/ui/universal/text.md#textstyle) for typography-specific properties (font size, weight, alignment).

```tsx
import { Host, Text } from '@expo/ui';

export default function StyledTextExample() {
  return (
    <Host matchContents>
      <Text textStyle={{ fontSize: 24, fontWeight: '700', textAlign: 'center' }}>Headline</Text>
    </Host>
  );
}
```

### Truncating long text

Use [`numberOfLines`](/versions/latest/sdk/ui/universal/text.md#numberoflines) to clamp long text with a trailing ellipsis.

```tsx
import { Host, Text } from '@expo/ui';

export default function TruncatedTextExample() {
  return (
    <Host style={{ flex: 1 }}>
      <Text numberOfLines={1}>
        A very long line of text that will be truncated when it does not fit on a single line.
      </Text>
    </Host>
  );
}
```

## API

```tsx
import { Text } from '@expo/ui';
```

## Component

### `Text`

Supported platforms: Android, iOS, Web.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[TextProps](https://reactnative.dev/docs/text#props)\>

A component for displaying styled text content.

Props for the [`Text`](#text) component.

TextProps

### `children`

Supported platforms: Android, iOS, Web.

Optional • Type: `string`

The text content to display.

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

### `numberOfLines`

Supported platforms: Android, iOS, Web.

Optional • Type: `number`

Maximum number of lines to display. Text is truncated with an ellipsis when exceeded.

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

### `style`

Supported platforms: Android, iOS, Web.

Optional • Type: [Pick](https://www.typescriptlang.org/docs/handbook/utility-types.html#picktype-keys)<[ViewStyle](https://reactnative.dev/docs/view-style-props), 'padding' | 'paddingHorizontal' | 'paddingVertical' | 'paddingTop' | 'paddingBottom' | 'paddingLeft' | 'paddingRight' | 'backgroundColor' | 'borderRadius' | 'borderWidth' | 'borderColor' | 'opacity' | 'width' | 'height'\>

Platform-agnostic style properties. These are translated to SwiftUI modifiers on iOS and Jetpack Compose modifiers on Android.

### `testID`

Supported platforms: Android, iOS, Web.

Optional • Type: `string`

Identifier used to locate the component in end-to-end tests.

### `textStyle`

Supported platforms: Android, iOS, Web.

Optional • Type: `{ color: string, fontFamily: string, fontSize: number, fontWeight: 'normal' | 'bold' | '100' | '200' | '300' | '400' | '500' | '600' | '700' | '800' | '900', letterSpacing: number, lineHeight: number, textAlign: 'center' | 'left' | 'right' }`

Text-specific styling (font, color, alignment).
