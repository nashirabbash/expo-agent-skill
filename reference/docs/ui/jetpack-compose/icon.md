---
title: "Icon"
description: "A Jetpack Compose Icon component for displaying icons."
source_url: "https://docs.expo.dev/versions/latest/sdk/ui/jetpack-compose/icon.md"
scraped_at: "2026-07-15T09:00:51.211070"
---

---
title: Icon
description: A Jetpack Compose Icon component for displaying icons.
sourceCodeUrl: 'https://github.com/expo/expo/tree/sdk-57/packages/expo-ui'
packageName: '@expo/ui'
platforms: ['android', 'expo-go']
---



This documentation is available as Markdown for AI agents and LLMs. See the [full Markdown index](/llms.txt) or append .md to any documentation URL.

# Icon

A Jetpack Compose Icon component for displaying icons.
Android, Included in Expo Go

> For cross-platform usage, see the universal [`Icon`](/versions/latest/sdk/ui/universal/icon.md) — it renders the appropriate native component per platform.

An icon component for rendering Material Symbol XML vector drawables in Jetpack Compose. The recommended source is [`@expo/material-symbols`](https://www.npmjs.com/package/@expo/material-symbols) — it ships Google's [Material Symbols](https://fonts.google.com/icons) as individual asset subpaths, so Metro only bundles the icons you actually import. For other styles (rounded, sharp, filled) or custom axes, the package's [CLI](/versions/latest/sdk/ui/jetpack-compose/icon.md#custom-styles-via-expomaterial-symbols-cli) downloads any variant directly into your project.

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

Optionally, install [`@expo/material-symbols`](https://www.npmjs.com/package/@expo/material-symbols) to use the bundled icons. For a different style or custom axes, see [Custom styles](/versions/latest/sdk/ui/jetpack-compose/icon.md#custom-styles-via-expomaterial-symbols-cli) — no install needed.

```sh
npx expo install @expo/material-symbols
```

## Usage

### Basic icon

Import any icon directly from its own subpath of `@expo/material-symbols` — each icon resolves to a Metro asset that `Icon` can render natively. For local XML files you add to your project, use `require()` instead (see [Custom styles](/versions/latest/sdk/ui/jetpack-compose/icon.md#custom-styles-via-expomaterial-symbols-cli) below).

```tsx
import { Host, Icon } from '@expo/ui/jetpack-compose';
import Home from '@expo/material-symbols/home.xml';

export default function BasicIcon() {
  return (
    <Host matchContents>
      <Icon source={Home} contentDescription="Home" />
    </Host>
  );
}
```

### Icon with tint color

Use the `tint` prop to apply a color overlay to the icon.

```tsx
import { Host, Icon } from '@expo/ui/jetpack-compose';
import Favorite from '@expo/material-symbols/favorite.xml';

export default function TintedIcon() {
  return (
    <Host matchContents>
      <Icon source={Favorite} tint="#6200ee" contentDescription="Favorite" />
    </Host>
  );
}
```

### Icon with size

Specify a custom size in dp using the `size` prop.

```tsx
import { Host, Icon } from '@expo/ui/jetpack-compose';
import Settings from '@expo/material-symbols/settings.xml';

export default function SizedIcon() {
  return (
    <Host matchContents>
      <Icon source={Settings} size={48} contentDescription="Settings" />
    </Host>
  );
}
```

### Custom styles via `@expo/material-symbols` CLI

`@expo/material-symbols` ships the **outlined** style with default axes. When you need a different style (`rounded`, `sharp`), a filled variant, or custom weight, grade, or optical size, use its CLI to fetch specific drawables straight from Google Fonts into your project.

```sh
npx @expo/material-symbols star home
npx @expo/material-symbols --style rounded star home
npx @expo/material-symbols --style sharp --fill favorite
npx @expo/material-symbols "https://fonts.google.com/icons?selected=Material+Symbols+Outlined:check_box:FILL@1;wght@300;GRAD@0;opsz@24"
```

| Option | Description | Default |
| --- | --- | --- |
| `-o, --output <dir>` | Output directory | `./assets` |
| `-s, --style <style>` | Icon style: `outlined`, `rounded`, `sharp` | `outlined` |
| `-f, --fill` | Use the filled variant |  |
| `-w, --weight <wght>` | Weight: `100`–`700` | `400` |
| `-g, --grade <grad>` | Grade: `-25`, `0`, `200` | `0` |
| `--opsz <size>` | Optical size: `20`, `24`, `40`, `48` | `24` |

The CLI writes ready-to-use XML vector drawables into your project. Load them with `require()` and pass them to `Icon`.

```tsx
import { Host, Icon } from '@expo/ui/jetpack-compose';

export default function CustomIcon() {
  return (
    <Host matchContents>
      <Icon source={require('./assets/star-rounded.xml')} size={32} contentDescription="Star" />
    </Host>
  );
}
```

## API

```tsx
import { Icon } from '@expo/ui/jetpack-compose';
```

## Component

### `Icon`

Supported platforms: Android.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[IconProps](#iconprops)\>

Displays an icon from an XML vector drawable or other image source.

The Icon component renders vector graphics and images with support for tinting, sizing, and accessibility features. On Android, it natively supports XML vector drawables loaded via Metro bundler using `require()`.

Example

Basic usage:

```tsx
import { Icon } from 'expo-ui';

<Icon source={require('./assets/home.xml')} />
```

Example

With styling:

```tsx
<Icon
  source={require('./assets/settings.xml')}
  size={24}
  tint="#007AFF"
  contentDescription="Settings icon"
/>
```

Example

With modifiers:

```tsx
<Icon
  source={require('./assets/star.xml')}
  size={32}
  modifiers={[
    padding(8),
    background('lightgray')
  ]}
/>
```

IconProps

### `contentDescription`

Supported platforms: Android.

Optional • Type: `string`

Accessibility label for the icon. Used by screen readers to describe the icon to users.

Example

```tsx
<Icon
  source={require('./assets/settings.xml')}
  contentDescription="Settings icon"
/>
```

### `modifiers`

Supported platforms: Android.

Optional • Type: `ModifierConfig[]`

Modifiers for the component. Allows you to apply layout and styling modifiers to the icon.

Example

```tsx
<Icon
  source={require('./assets/icon.xml')}
  modifiers={[
    padding(8),
    background('lightgray')
  ]}
/>
```

### `size`

Supported platforms: Android.

Optional • Type: `number`

The size of the icon in density-independent pixels (dp). If not specified, the icon will use its intrinsic size.

Example

```tsx
<Icon source={require('./assets/settings.xml')} size={24} />
```

### `source`

Supported platforms: Android.

Type: [ImageSourcePropType](https://reactnative.dev/docs/image#imagesource)

The source of the icon. Can be a URI string or the result of `require()`. On Android, supports XML vector drawables loaded via Metro bundler.

Example

```tsx
<Icon source={require('./assets/home.xml')} />
<Icon source={{ uri: 'file:///path/to/icon.xml' }} />
```

### `tint`

Supported platforms: Android.

Optional • Literal type: `union`

The tint color to apply to the icon. Accepts hex strings, named colors, or RGB arrays.

-   When omitted, the icon inherits the color from the surrounding `LocalContentColor` (e.g. the toolbar/FAB content color).
-   When set to `null`, no tint is applied — the icon is drawn with its original colors (`Color.Unspecified`). Use this for multicolored icons.

Example

```tsx
<Icon source={require('./assets/star.xml')} tint="#007AFF" />
<Icon source={require('./assets/star.xml')} tint="blue" />
<Icon source={require('./assets/multicolor.xml')} tint={null} />
```

Acceptable values are: [ColorValue](https://reactnative.dev/docs/colors) | `null`
