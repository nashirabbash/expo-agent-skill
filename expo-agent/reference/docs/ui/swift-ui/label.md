---
title: "Label"
description: "A SwiftUI Label component for displaying text with an icon."
source_url: "https://docs.expo.dev/versions/latest/sdk/ui/swift-ui/label.md"
scraped_at: "2026-07-15T08:59:32.691615"
---

---
title: Label
description: A SwiftUI Label component for displaying text with an icon.
sourceCodeUrl: 'https://github.com/expo/expo/tree/sdk-57/packages/expo-ui'
packageName: '@expo/ui'
platforms: ['ios', 'tvos', 'expo-go']
---



This documentation is available as Markdown for AI agents and LLMs. See the [full Markdown index](/llms.txt) or append .md to any documentation URL.

# Label

A SwiftUI Label component for displaying text with an icon.
iOS, tvOS, Included in Expo Go

Expo UI Label matches the official SwiftUI [Label API](https://developer.apple.com/documentation/swiftui/label) and displays a title alongside an icon.

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

### Basic label with SF Symbol

```tsx
import { Host, Label } from '@expo/ui/swift-ui';

export default function BasicLabelExample() {
  return (
    <Host matchContents>
      <Label title="Favorites" systemImage="star.fill" />
    </Host>
  );
}
```

### With custom icon

Use the `icon` prop to provide a custom React node as the icon instead of an SF Symbol.

```tsx
import { Host, Label, Image } from '@expo/ui/swift-ui';

export default function LabelCustomIconExample() {
  return (
    <Host matchContents>
      <Label title="Custom Icon" icon={<Image systemName="sparkles" size={20} color="purple" />} />
    </Host>
  );
}
```

### Icon only

Use the [`labelStyle`](/versions/latest/sdk/ui/swift-ui/modifiers.md#labelstylestyle) modifier with `iconOnly` to display only the icon. Always provide a `title` for accessibility even though it won't be visible.

```tsx
import { Host, Label } from '@expo/ui/swift-ui';
import { labelStyle } from '@expo/ui/swift-ui/modifiers';

export default function LabelIconOnlyExample() {
  return (
    <Host matchContents>
      <Label title="Settings" systemImage="gear" modifiers={[labelStyle('iconOnly')]} />
    </Host>
  );
}
```

## API

```tsx
import { Label } from '@expo/ui/swift-ui';
```

## Component

### `Label`

Supported platforms: iOS, tvOS.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[LabelProps](#labelprops)\>

Renders a native label view, which could be used in a list or section.

LabelProps

### `children`

Supported platforms: iOS, tvOS.

Optional • Type: [ReactNode](https://reactnative.dev/docs/react-node)

Custom title view. Accepts any React node (for example, a `VStack` with title and subtitle). When provided, this takes precedence over `title`.

> **Deprecated:** Use `foregroundStyle` modifier instead.

### `color`

Supported platforms: iOS, tvOS.

Optional • Type: [ColorValue](https://reactnative.dev/docs/colors)

The color of the label icon.

### `icon`

Supported platforms: iOS, tvOS.

Optional • Type: [ReactNode](https://reactnative.dev/docs/react-node)

Custom icon view to be displayed in the label. When provided, this takes precedence over `systemImage`.

### `systemImage`

Supported platforms: iOS, tvOS.

Optional • Type: [SFSymbols7_0](https://github.com/nandorojo/sf-symbols-typescript)

The name of the SFSymbol to be displayed in the label.

### `title`

Supported platforms: iOS, tvOS.

Optional • Type: `string`

The title text to be displayed in the label.

#### Inherited Props

-   [CommonViewModifierProps](/versions/latest/sdk/ui/swift-ui/modifiers.md)
