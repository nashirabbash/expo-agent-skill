---
title: "Icon"
description: "A platform-native icon — SF Symbol on iOS, Material Symbol on Android."
source_url: "https://docs.expo.dev/versions/latest/sdk/ui/universal/icon.md"
scraped_at: "2026-07-15T09:01:38.613062"
---

---
title: Icon
description: A platform-native icon — SF Symbol on iOS, Material Symbol on Android.
sourceCodeUrl: 'https://github.com/expo/expo/tree/sdk-57/packages/expo-ui'
packageName: '@expo/ui'
platforms: ['android', 'ios', 'expo-go']
---



This documentation is available as Markdown for AI agents and LLMs. See the [full Markdown index](/llms.txt) or append .md to any documentation URL.

# Icon

A platform-native icon — SF Symbol on iOS, Material Symbol on Android.
Android, iOS, Included in Expo Go

A platform-native icon. On Android, it renders a Material Symbol XML vector drawable (recommended source: [`@expo/material-symbols`](https://www.npmjs.com/package/@expo/material-symbols)). On iOS, it renders an [SF Symbol](https://developer.apple.com/sf-symbols/).

> **Note:** `Icon` does not render on web.

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

Optionally, install [`@expo/material-symbols`](https://www.npmjs.com/package/@expo/material-symbols) to use the bundled icons on Android. For a different style or custom axes, see [Custom styles on the Jetpack Compose Icon page](/versions/latest/sdk/ui/jetpack-compose/icon.md#custom-styles-via-expomaterial-symbols-cli) — no install needed.

```sh
npx expo install @expo/material-symbols
```

## Usage

### Cross-platform icon with `Icon.select`

[`Icon.select`](/versions/latest/sdk/ui/universal/icon.md#selectspec) picks the right asset for the current platform. Pair it with [`@expo/ui/babel-plugin`](https://github.com/expo/expo/tree/main/packages/expo-ui/plugin) (auto-loaded by `babel-preset-expo`) so Metro can tree-shake the unused side per platform.

```tsx
import { Host, Icon } from '@expo/ui';

export default function IconSelectExample() {
  return (
    <Host matchContents>
      <Icon
        name={Icon.select({
          ios: 'star.fill',
          android: import('@expo/material-symbols/star.xml'),
        })}
        size={32}
        color="orange"
      />
    </Host>
  );
}
```

### Hoisted `Icon.select`

Hoist the [`Icon.select`](/versions/latest/sdk/ui/universal/icon.md#selectspec) call when reusing the same icon across multiple call sites.

```tsx
import { Host, Row, Icon } from '@expo/ui';

const STAR = Icon.select({
  ios: 'star.fill',
  android: import('@expo/material-symbols/star.xml'),
});

export default function HoistedIconExample() {
  return (
    <Host matchContents>
      <Row spacing={4}>
        <Icon name={STAR} size={20} color="gold" />
        <Icon name={STAR} size={20} color="gold" />
        <Icon name={STAR} size={20} color="gold" />
      </Row>
    </Host>
  );
}
```

### Platform-specific files

Inside an **.android.tsx** file, import the XML asset directly. Inside an **.ios.tsx** file, pass the SF Symbol name as a string.

```tsx
import StarIcon from '@expo/material-symbols/star.xml';
import { Host, Icon } from '@expo/ui';

export default function StarRow() {
  return (
    <Host matchContents>
      <Icon name={StarIcon} size={24} />
    </Host>
  );
}
```

```tsx
import { Host, Icon } from '@expo/ui';

export default function StarRow() {
  return (
    <Host matchContents>
      <Icon name="star.fill" size={24} />
    </Host>
  );
}
```

## API

```tsx
import { Icon } from '@expo/ui';
```

## Component

### `Icon`

Supported platforms: Android, iOS.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[IconProps](#iconprops)\>

A platform-native icon. Renders an XML vector drawable (typically from `@expo/material-symbols`) on Android and an SF Symbol on iOS.

Example

```tsx
const STAR = Icon.select({
  ios: 'star.fill',
  android: import('@expo/material-symbols/star.xml'),
});

<Icon name={STAR} size={24} color="orange" />
```

Example

```tsx
<Icon
  name={Icon.select({
    ios: 'star.fill',
    android: import('@expo/material-symbols/star.xml'),
  })}
  size={24}
/>
```

Example

Both sides ship to both platforms. Prefer `Icon.select` when bundle size matters.

```tsx
<Icon
  name={{
    ios: 'star.fill',
    android: require('@expo/material-symbols/star.xml'),
  }}
  size={24}
/>
```

Example

```tsx
import StarIcon from '@expo/material-symbols/star.xml';

<Icon name={StarIcon} size={24} />
```

Example

```tsx
<Icon name="star.fill" size={24} />
```

Props for the [`Icon`](#icon) component.

IconProps

### `accessibilityLabel`

Supported platforms: Android.

Optional • Type: `string`

Accessibility label for screen readers. On Android, maps to `contentDescription`. iOS accessibility is not yet wired up.

### `color`

Supported platforms: Android, iOS.

Optional • Type: [ColorValue](https://reactnative.dev/docs/colors)

Tint color applied to the icon.

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

### `name`

Supported platforms: Android, iOS.

Type: [IconName](#iconname)

Icon source. Android expects an XML vector drawable asset (typically from `@expo/material-symbols`); iOS expects an SF Symbol string.

Use [`Icon.select`](#selectspec) for a cross-platform definition.

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

### `size`

Supported platforms: Android, iOS.

Optional • Type: `number`

Icon size in dp (Android) / points (iOS). When omitted, the icon uses its intrinsic size.

### `style`

Supported platforms: Android, iOS, Web.

Optional • Type: [Pick](https://www.typescriptlang.org/docs/handbook/utility-types.html#picktype-keys)<[ViewStyle](https://reactnative.dev/docs/view-style-props), 'padding' | 'paddingHorizontal' | 'paddingVertical' | 'paddingTop' | 'paddingBottom' | 'paddingLeft' | 'paddingRight' | 'backgroundColor' | 'borderRadius' | 'borderWidth' | 'borderColor' | 'opacity' | 'width' | 'height'\>

Platform-agnostic style properties. These are translated to SwiftUI modifiers on iOS and Jetpack Compose modifiers on Android.

### `testID`

Supported platforms: Android, iOS, Web.

Optional • Type: `string`

Identifier used to locate the component in end-to-end tests.

## Component Methods

### `select(spec)`

Supported platforms: Android, iOS.

| Parameter | Type |
| --- | --- |
| `spec` | [IconSelectSpec](#iconselectspec) |

  

Picks the icon source for the current platform — `android` on Android, `ios` on iOS.

Pair with `@expo/ui/babel-plugin` to strip the unused side per platform.

Returns: `SFSymbols7_0 | ImageSourcePropType`

Example

```tsx
const STAR = Icon.select({
  ios: 'star.fill',
  android: import('@expo/material-symbols/star.xml'),
});

<Icon name={STAR} size={24} />
```

## Interfaces

### `IconSelectSpec`

Supported platforms: Android, iOS.

Argument shape accepted by [`Icon.select`](#selectspec).

The `android` slot accepts either a synchronous `require()` result or a dynamic `import('*.xml')` expression. The latter is preferred because TypeScript validates the literal path through the package's `exports` map, catching typos at compile time. The accompanying Babel plugin (`@expo/ui/babel-plugin`, auto-loaded by `babel-preset-expo`) rewrites the `import()` to a `require()` so Metro can still tree-shake the unused side.

| Property | Type | Description |
| --- | --- | --- |
| android | [ImageSourcePropType](https://reactnative.dev/docs/image#imagesource) | [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<{ default: [ImageSourcePropType](https://reactnative.dev/docs/image#imagesource) }\> | - |
| ios | [SFSymbols7_0](https://github.com/nandorojo/sf-symbols-typescript) | - |

## Types

### `IconName`

Supported platforms: Android, iOS.

A platform-specific icon definition.

Pass a primitive (`require()`'d XML asset on Android, `string` SF Symbol on iOS) or use [`Icon.select`](#selectspec) for a cross-platform definition.

The plain object form (`{ ios, android }`) is also accepted but does not tree-shake — the Android bundle still includes the iOS asset and vice versa. Prefer [`Icon.select`](#selectspec) so the `babel-preset-expo` plugin can rewrite the call into a `Platform.OS` ternary that Metro DCE can fold per platform.

Type: [SFSymbol](https://github.com/nandorojo/sf-symbols-typescript) or [ImageSourcePropType](https://reactnative.dev/docs/image#imagesource) or `object` shaped as below:

| Property | Type | Description |
| --- | --- | --- |
| android | [ImageSourcePropType](https://reactnative.dev/docs/image#imagesource) | - |
| ios | [SFSymbol](https://github.com/nandorojo/sf-symbols-typescript) | - |
