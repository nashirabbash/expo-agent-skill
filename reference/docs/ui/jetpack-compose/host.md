---
title: "Host"
description: "A Jetpack Compose Host component for bridging React Native and Jetpack Compose."
source_url: "https://docs.expo.dev/versions/latest/sdk/ui/jetpack-compose/host.md"
scraped_at: "2026-07-15T09:00:42.357496"
---

---
title: Host
description: A Jetpack Compose Host component for bridging React Native and Jetpack Compose.
sourceCodeUrl: 'https://github.com/expo/expo/tree/sdk-57/packages/expo-ui'
packageName: '@expo/ui'
platforms: ['android', 'expo-go']
---



This documentation is available as Markdown for AI agents and LLMs. See the [full Markdown index](/llms.txt) or append .md to any documentation URL.

# Host

A Jetpack Compose Host component for bridging React Native and Jetpack Compose.
Android, Included in Expo Go

> For cross-platform usage, see the universal [`Host`](/versions/latest/sdk/ui/universal/host.md) — it renders the appropriate native component per platform.

The `Host` component is the bridge between React Native and Jetpack Compose. Every Jetpack Compose component from `@expo/ui/jetpack-compose` must be wrapped in a `Host` to render correctly.

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

### Match contents

Use the `matchContents` prop to make the `Host` size itself to fit the content. You can pass a boolean or an object to control vertical and horizontal sizing independently.

```tsx
import { Host, Button } from '@expo/ui/jetpack-compose';

export default function MatchContents() {
  return (
    <Host matchContents>
      <Button onClick={() => console.log('Pressed')}>Sized to content</Button>
    </Host>
  );
}
```

> **Note:** Do not use `matchContents` on the same axis as a scrollable child (`LazyRow`, `LazyColumn`, `Carousel`, or anything using `Modifier.horizontalScroll`/`verticalScroll`). Scrollables require a finite max constraint on their scroll axis and `matchContents` propagates an unbounded one.

The following example crashes:

```tsx
import { Host, LazyRow, Text } from '@expo/ui/jetpack-compose';

export default function MatchContentsCrash() {
  return (
    <Host matchContents>
      <LazyRow>
        {Array.from({ length: 5 }).map((_, i) => (
          <Text key={i}>Item {i}</Text>
        ))}
      </LazyRow>
    </Host>
  );
}
```

Either drop `matchContents` on the scroll axis or give the `Host` a finite size on that axis via `style`:

```tsx
import { Host, LazyRow, Text } from '@expo/ui/jetpack-compose';

export default function MatchContentsFix() {
  return (
    <Host matchContents={{ vertical: true }} style={{ width: '100%' }}>
      <LazyRow>
        {Array.from({ length: 5 }).map((_, i) => (
          <Text key={i}>Item {i}</Text>
        ))}
      </LazyRow>
    </Host>
  );
}
```

### With style

Apply standard React Native styles to the `Host` wrapper.

```tsx
import { Host, Button } from '@expo/ui/jetpack-compose';

export default function HostWithStyle() {
  return (
    <Host style={{ padding: 16, backgroundColor: '#f0f0f0', borderRadius: 8 }}>
      <Button onClick={() => console.log('Pressed')}>Styled host</Button>
    </Host>
  );
}
```

## API

```tsx
import { Host } from '@expo/ui/jetpack-compose';
```

## Component

### `Host`

Supported platforms: Android.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[HostProps](#hostprops)\>

HostProps

### `children`

Supported platforms: Android.

Type: [ReactNode](https://reactnative.dev/docs/react-node)

### `colorScheme`

Supported platforms: Android.

Optional • Type: `ColorSchemeName`

The color scheme of the host view. `'light'` / `'dark'` force a specific appearance; omitted follows the device setting. The palette itself follows the device wallpaper on Android 12+ (Material You) or the static Material 3 baseline otherwise — unless [`seedColor`](#seedcolor) is set.

### `ignoreSafeAreaKeyboardInsets`

Supported platforms: Android.

Optional • Type: `boolean` • Default: `false`

When `true`, the Compose content will not perform keyboard avoidance behaviour when keyboard is shown. Can be only set once on mount.

### `layoutDirection`

Supported platforms: Android.

Optional • Literal type: `string`

The layout direction for the content. Defaults to the current locale direction from I18nManager.

Acceptable values are: `'leftToRight'` | `'rightToLeft'`

### `matchContents`

Supported platforms: Android.

Optional • Literal type: `union` • Default: `false`

When true, the host view will update its size in the React Native view tree to match the content's layout from Jetpack Compose. Can be only set once on mount.

Acceptable values are: `boolean` | `{ horizontal: boolean, vertical: boolean }`

### `onLayoutContent`

Supported platforms: Android.

Optional • Type: `(event: { nativeEvent: { height: number, width: number } }) => void`

Callback function that is triggered when the Jetpack Compose content completes its layout. Provides the current dimensions of the content, which may change as the content updates.

### `pointerEvents`

Supported platforms: Android.

Optional • Literal type: `string`

Acceptable values are: `'box-none'` | `'none'` | `'box-only'` | `'auto'`

### `seedColor`

Supported platforms: Android.

Optional • Type: [ColorValue](https://reactnative.dev/docs/colors)

Seed color used to generate a Material 3 palette (`SchemeTonalSpot`) for this host. Combines with `colorScheme` (`'light'` / `'dark'` or omitted) to produce a seeded palette that themes Compose children and is available to descendants via `useMaterialColors()`.

### `style`

Supported platforms: Android.

Optional • Type: StyleProp<[ViewStyle](https://reactnative.dev/docs/view-style-props)\>

### `useViewportSizeMeasurement`

Supported platforms: Android.

Optional • Type: `boolean` • Default: `false`

When true and no explicit size is provided, the host will use the viewport size as the proposed size for Compose layout. This is particularly useful for views that need to fill their available space.

#### Inherited Props

-   `PrimitiveBaseProps`
