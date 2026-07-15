---
title: "Link"
description: "A SwiftUI Link component for displaying clickable links."
source_url: "https://docs.expo.dev/versions/latest/sdk/ui/swift-ui/link.md"
scraped_at: "2026-07-15T08:59:31.837252"
---

---
title: Link
description: A SwiftUI Link component for displaying clickable links.
sourceCodeUrl: 'https://github.com/expo/expo/tree/sdk-57/packages/expo-ui'
packageName: '@expo/ui'
platforms: ['ios', 'tvos', 'expo-go']
---



This documentation is available as Markdown for AI agents and LLMs. See the [full Markdown index](/llms.txt) or append .md to any documentation URL.

# Link

A SwiftUI Link component for displaying clickable links.
iOS, tvOS, Included in Expo Go

Expo UI Link matches the official SwiftUI [Link API](https://developer.apple.com/documentation/swiftui/link).

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

### Basic link

```tsx
import { Host, Link } from '@expo/ui/swift-ui';

export default function BasicLinkExample() {
  return (
    <Host style={{ flex: 1 }}>
      <Link label="Visit Expo" destination="https://expo.dev" />
    </Host>
  );
}
```

### Custom label content

You can pass custom components as `children` for more complex link label content.

```tsx
import { Host, Link, VStack, Image, Text } from '@expo/ui/swift-ui';

export default function CustomContentExample() {
  return (
    <Host matchContents>
      <Link destination="https://expo.dev">
        <VStack spacing={4}>
          <Image systemName="link" />
          <Text>Expo</Text>
        </VStack>
      </Link>
    </Host>
  );
}
```

## API

```tsx
import { Link } from '@expo/ui/swift-ui';
```

## Component

### `Link`

Supported platforms: iOS, tvOS.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[LinkProps](#linkprops)\>

Displays a native link component.

Example

```tsx
import { Link } from '@expo/ui/swift-ui';
import { foregroundStyle, font } from '@expo/ui/swift-ui/modifiers';

<Link
  label="Open"
  destination="https://expo.dev"
  modifiers={[
    foregroundStyle('red'),
    font({ size: 24, weight: 'bold' })
  ]}
/>
```

LinkProps

### `children`

Supported platforms: iOS, tvOS.

Optional • Literal type: `union`

Custom content for the link label. Use this for custom label views. Only nested elements are supported, not plain strings.

Acceptable values are: `ReactElement<unknown, string | JSXElementConstructor<any>>` | `ReactElement[]`

### `destination`

Supported platforms: iOS, tvOS.

Type: `string`

The URL for the link.

### `label`

Supported platforms: iOS, tvOS.

Optional • Type: `string`

The text label for the Link. Use this for simple text links.

#### Inherited Props

-   [CommonViewModifierProps](/versions/latest/sdk/ui/swift-ui/modifiers.md)
