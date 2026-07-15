---
title: "Collapsible"
description: "A labelled tappable header that toggles visibility of its content."
source_url: "https://docs.expo.dev/versions/latest/sdk/ui/universal/collapsible.md"
scraped_at: "2026-07-15T09:01:43.543611"
---

---
title: Collapsible
description: A labelled tappable header that toggles visibility of its content.
sourceCodeUrl: 'https://github.com/expo/expo/tree/sdk-57/packages/expo-ui'
packageName: '@expo/ui'
platforms: ['android', 'ios', 'web', 'expo-go']
---



This documentation is available as Markdown for AI agents and LLMs. See the [full Markdown index](/llms.txt) or append .md to any documentation URL.

# Collapsible

A labelled tappable header that toggles visibility of its content.
Android, iOS, Web, Included in Expo Go

`Collapsible` is a primitive that shows or hides its content with a tap on a labelled header. Controlled via [`isOpen`](/versions/latest/sdk/ui/universal/collapsible.md#isopen) and [`onOpenChange`](/versions/latest/sdk/ui/universal/collapsible.md#onopenchange) — each `Collapsible` manages independent state.

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

### Basic collapsible

```tsx
import { useState } from 'react';
import { Host, Column, Collapsible, Text } from '@expo/ui';

export default function CollapsibleExample() {
  const [open, setOpen] = useState(false);

  return (
    <Host style={{ flex: 1 }}>
      <Column spacing={8} style={{ padding: 16 }}>
        <Collapsible isOpen={open} onOpenChange={setOpen} label="About">
          <Text>
            A primitive that toggles visibility of its content via a labelled tappable header.
          </Text>
        </Collapsible>
      </Column>
    </Host>
  );
}
```

### Accordion (one section open at a time)

Wire each `Collapsible`'s `isOpen` to a shared parent value. The component doesn't enforce exclusivity — composition is up to the consumer.

```tsx
import { useState } from 'react';
import { Host, Column, Collapsible, Text } from '@expo/ui';

type Section = 'a' | 'b' | 'c' | null;

export default function CollapsibleAccordionExample() {
  const [openSection, setOpenSection] = useState<Section>('a');

  return (
    <Host style={{ flex: 1 }}>
      <Column spacing={8} style={{ padding: 16 }}>
        <Collapsible
          isOpen={openSection === 'a'}
          onOpenChange={open => setOpenSection(open ? 'a' : null)}
          label="Section A">
          <Text>Opening B or C closes this one.</Text>
        </Collapsible>
        <Collapsible
          isOpen={openSection === 'b'}
          onOpenChange={open => setOpenSection(open ? 'b' : null)}
          label="Section B">
          <Text>Opening A or C closes this one.</Text>
        </Collapsible>
        <Collapsible
          isOpen={openSection === 'c'}
          onOpenChange={open => setOpenSection(open ? 'c' : null)}
          label="Section C">
          <Text>Opening A or B closes this one.</Text>
        </Collapsible>
      </Column>
    </Host>
  );
}
```

## API

```tsx
import { Collapsible } from '@expo/ui';
```

## Component

### `Collapsible`

Supported platforms: Android, iOS, Web.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[CollapsibleProps](#collapsibleprops)\>

A primitive that toggles visibility of its content via a labelled tappable header. Controlled via `isOpen` + `onOpenChange`.

Props for the [`Collapsible`](#collapsible) component, a primitive that shows or hides its content with a tap on a labelled header.

CollapsibleProps

### `children`

Supported platforms: Android, iOS, Web.

Optional • Type: [ReactNode](https://reactnative.dev/docs/react-node)

Content rendered when `isOpen` is `true`.

### `isOpen`

Supported platforms: Android, iOS, Web.

Type: `boolean`

Whether the content is currently expanded.

### `label`

Supported platforms: Android, iOS, Web.

Optional • Type: `string`

Text rendered in the tappable header.

### `labelStyle`

Supported platforms: Android, iOS, Web.

Optional • Type: `{ color: string, fontFamily: string, fontSize: number, fontWeight: 'normal' | 'bold' | '100' | '200' | '300' | '400' | '500' | '600' | '700' | '800' | '900', letterSpacing: number, lineHeight: number, textAlign: 'center' | 'left' | 'right' }`

Text-specific styling for the tappable header label.

### `onOpenChange`

Supported platforms: Android, iOS, Web.

Type: `(isOpen: boolean) => void`

Called when the user taps the header to toggle the open state.
