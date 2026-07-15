---
title: "Badge"
description: "A Jetpack Compose Badge component for displaying status indicators and counts."
source_url: "https://docs.expo.dev/versions/latest/sdk/ui/jetpack-compose/badge.md"
scraped_at: "2026-07-15T09:00:43.938883"
---

---
title: Badge
description: A Jetpack Compose Badge component for displaying status indicators and counts.
sourceCodeUrl: 'https://github.com/expo/expo/tree/sdk-57/packages/expo-ui'
packageName: '@expo/ui'
platforms: ['android', 'expo-go']
---



This documentation is available as Markdown for AI agents and LLMs. See the [full Markdown index](/llms.txt) or append .md to any documentation URL.

# Badge

A Jetpack Compose Badge component for displaying status indicators and counts.
Android, Included in Expo Go

Expo UI Badge matches the official Jetpack Compose [`Badge`](https://developer.android.com/develop/ui/compose/components/badges) API. It renders as a small colored indicator dot, or with content such as a count number.

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

### Indicator dot

A badge with no children renders as a small dot indicator.

```tsx
import { Host, Badge } from '@expo/ui/jetpack-compose';

export default function BadgeDot() {
  return (
    <Host matchContents>
      <Badge />
    </Host>
  );
}
```

### Badge with count

Pass a `Text` child to display a number or label.

```tsx
import { Host, Badge, Text } from '@expo/ui/jetpack-compose';

export default function BadgeCount() {
  return (
    <Host matchContents>
      <Badge containerColor="#EF5350" contentColor="#FFFFFF">
        <Text>3</Text>
      </Badge>
    </Host>
  );
}
```

## API

```tsx
import { Badge } from '@expo/ui/jetpack-compose';
```

## Component

### `Badge`

Supported platforms: Android.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[BadgeProps](#badgeprops)\>

A badge component matching Compose's `Badge`. Renders as a small colored indicator dot, or with content (for example, a count).

> **See:** [Jetpack Compose Badge](https://developer.android.com/develop/ui/compose/components/badges)

BadgeProps

### `children`

Supported platforms: Android.

Optional • Type: [ReactNode](https://reactnative.dev/docs/react-node)

Optional content inside the badge (for example, a `Text` with a count). When omitted, renders as a small indicator dot.

### `containerColor`

Supported platforms: Android.

Optional • Type: [ColorValue](https://reactnative.dev/docs/colors) • Default: `BadgeDefaults.containerColor`

Background color of the badge.

### `contentColor`

Supported platforms: Android.

Optional • Type: [ColorValue](https://reactnative.dev/docs/colors) • Default: `BadgeDefaults.contentColor`

Content color inside the badge (text/icon tint).

### `modifiers`

Supported platforms: Android.

Optional • Type: `ModifierConfig[]`

Modifiers for the component.
