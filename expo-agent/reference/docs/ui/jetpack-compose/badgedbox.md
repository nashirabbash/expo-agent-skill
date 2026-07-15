---
title: "BadgedBox"
description: "A Jetpack Compose BadgedBox component for overlaying badges on content."
source_url: "https://docs.expo.dev/versions/latest/sdk/ui/jetpack-compose/badgedbox.md"
scraped_at: "2026-07-15T09:00:31.218459"
---

---
title: BadgedBox
description: A Jetpack Compose BadgedBox component for overlaying badges on content.
sourceCodeUrl: 'https://github.com/expo/expo/tree/sdk-57/packages/expo-ui'
packageName: '@expo/ui'
platforms: ['android', 'expo-go']
---



This documentation is available as Markdown for AI agents and LLMs. See the [full Markdown index](/llms.txt) or append .md to any documentation URL.

# BadgedBox

A Jetpack Compose BadgedBox component for overlaying badges on content.
Android, Included in Expo Go

Expo UI BadgedBox matches the official Jetpack Compose [`BadgedBox`](https://developer.android.com/develop/ui/compose/components/badges) API. It overlays a badge on top of content such as an icon.

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

### Icon with badge count

```tsx
import { Host, Badge, BadgedBox, Icon, Text } from '@expo/ui/jetpack-compose';

// Replace with your own vector drawable asset
const mailIcon = require('./assets/mail.xml');

export default function IconWithBadge() {
  return (
    <Host matchContents>
      <BadgedBox>
        <BadgedBox.Badge>
          <Badge>
            <Text>5</Text>
          </Badge>
        </BadgedBox.Badge>
        <Icon source={mailIcon} size={24} />
      </BadgedBox>
    </Host>
  );
}
```

### Interactive counter

```tsx
import { useState } from 'react';
import { Host, Badge, BadgedBox, Icon, Button, Text, Column } from '@expo/ui/jetpack-compose';

// Replace with your own vector drawable asset
const cartIcon = require('./assets/cart.xml');

export default function InteractiveBadge() {
  const [count, setCount] = useState(0);

  return (
    <Host matchContents>
      <Column>
        <BadgedBox>
          <BadgedBox.Badge>
            {count > 0 ? (
              <Badge>
                <Text>{String(count)}</Text>
              </Badge>
            ) : null}
          </BadgedBox.Badge>
          <Icon source={cartIcon} size={24} />
        </BadgedBox>
        <Button onClick={() => setCount(c => c + 1)}>
          <Text>Add item</Text>
        </Button>
      </Column>
    </Host>
  );
}
```

## API

```tsx
import { BadgedBox } from '@expo/ui/jetpack-compose';
```

## Component

### `BadgedBox`

Supported platforms: Android.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[BadgedBoxProps](#badgedboxprops)\>

A badged box matching Compose's `BadgedBox`. Overlays a badge on top of content (for example, an icon).

> **See:** [Jetpack Compose BadgedBox](https://developer.android.com/develop/ui/compose/components/badges)

BadgedBoxProps

### `children`

Supported platforms: Android.

Optional • Type: [ReactNode](https://reactnative.dev/docs/react-node)

Children containing the main content and a `BadgedBox.Badge` slot.

### `modifiers`

Supported platforms: Android.

Optional • Type: `ModifierConfig[]`

Modifiers for the component.
