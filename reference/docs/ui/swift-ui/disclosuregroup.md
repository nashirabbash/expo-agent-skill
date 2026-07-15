---
title: "DisclosureGroup"
description: "A SwiftUI DisclosureGroup component for displaying expandable content."
source_url: "https://docs.expo.dev/versions/latest/sdk/ui/swift-ui/disclosuregroup.md"
scraped_at: "2026-07-15T08:59:39.181724"
---

---
title: DisclosureGroup
description: A SwiftUI DisclosureGroup component for displaying expandable content.
sourceCodeUrl: 'https://github.com/expo/expo/tree/sdk-57/packages/expo-ui'
packageName: '@expo/ui'
platforms: ['ios', 'expo-go']
---



This documentation is available as Markdown for AI agents and LLMs. See the [full Markdown index](/llms.txt) or append .md to any documentation URL.

# DisclosureGroup

A SwiftUI DisclosureGroup component for displaying expandable content.
iOS, Included in Expo Go

Expo UI DisclosureGroup matches the official SwiftUI [DisclosureGroup API](https://developer.apple.com/documentation/swiftui/disclosuregroup) and displays a disclosure indicator that reveals or hides content.

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

### Basic disclosure group

`DisclosureGroup` is most commonly used inside a [`Form`](/versions/latest/sdk/ui/swift-ui/form.md) so it picks up the standard iOS list styling with a chevron indicator.

```tsx
import { useState } from 'react';
import { DisclosureGroup, Form, Host, Section, Text } from '@expo/ui/swift-ui';

export default function BasicDisclosureGroupExample() {
  const [isExpanded, setIsExpanded] = useState(true);
  return (
    <Host style={{ flex: 1 }}>
      <Form>
        <Section>
          <DisclosureGroup
            label="Advanced settings"
            isExpanded={isExpanded}
            onIsExpandedChange={setIsExpanded}>
            <Text>Auto-update apps</Text>
            <Text>App downloads</Text>
            <Text>Offload unused apps</Text>
          </DisclosureGroup>
        </Section>
      </Form>
    </Host>
  );
}
```

### Initially expanded

Set `isExpanded` to `true` initially to show the content by default.

```tsx
import { useState } from 'react';
import { Host, DisclosureGroup, Text } from '@expo/ui/swift-ui';

export default function InitiallyExpandedExample() {
  const [isExpanded, setIsExpanded] = useState(true);

  return (
    <Host matchContents>
      <DisclosureGroup label="Details" isExpanded={isExpanded} onIsExpandedChange={setIsExpanded}>
        <Text>This content is visible by default.</Text>
      </DisclosureGroup>
    </Host>
  );
}
```

### Custom label

Use `DisclosureGroup.Label` when the label needs custom SwiftUI content or modifiers instead of the `label` string prop.

```tsx
import { useState } from 'react';
import { DisclosureGroup, Form, Host, Section, Text } from '@expo/ui/swift-ui';
import { font, foregroundStyle } from '@expo/ui/swift-ui/modifiers';

export default function CustomLabelDisclosureGroupExample() {
  const [isExpanded, setIsExpanded] = useState(false);

  return (
    <Host style={{ flex: 1 }}>
      <Form>
        <Section>
          <DisclosureGroup isExpanded={isExpanded} onIsExpandedChange={setIsExpanded}>
            <DisclosureGroup.Label>
              <Text modifiers={[font({ weight: 'semibold' }), foregroundStyle('#0a7ea4')]}>
                Network options
              </Text>
            </DisclosureGroup.Label>
            <Text>Wi-Fi</Text>
            <Text>Bluetooth</Text>
            <Text>Cellular data</Text>
          </DisclosureGroup>
        </Section>
      </Form>
    </Host>
  );
}
```

## API

```tsx
import { DisclosureGroup } from '@expo/ui/swift-ui';
```

## Component

### `DisclosureGroup`

Supported platforms: iOS.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[DisclosureGroupProps](#disclosuregroupprops)\>

DisclosureGroupProps

### `children`

Supported platforms: iOS.

Type: [ReactNode](https://reactnative.dev/docs/react-node)

### `isExpanded`

Supported platforms: iOS.

Optional • Type: `boolean`

Controls whether the disclosure group is expanded.

### `label`

Supported platforms: iOS.

Optional • Type: `string`

Text label for the disclosure group. Use `DisclosureGroup.Label` for custom label content.

### `onIsExpandedChange`

Supported platforms: iOS.

Optional • Type: `(isExpanded: boolean) => void`

A callback that is called when the expansion state changes.

#### Inherited Props

-   [CommonViewModifierProps](/versions/latest/sdk/ui/swift-ui/modifiers.md)
